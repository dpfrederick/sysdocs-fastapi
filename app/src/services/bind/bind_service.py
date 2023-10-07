import subprocess
from datetime import datetime
from typing import List

from ...models import Record, Zone
from ...providers.database import DatabaseProvider


class BindService:
    _instance = None

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of BindService."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def generate_bind_config(self, zones: List[Zone], records: List[Record]):
        """Generate BIND configuration as a string and write to named.conf."""
        config_str = "; Auto-generated BIND config file\n"
        for zone in zones:
            config_str += f'zone "{zone.name}" IN {{\n'
            config_str += "  type master;\n"
            config_str += f'  file "/etc/bind/db.{zone.name}";\n'
            config_str += "};\n"

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            subprocess.run(
                [
                    "mv",
                    "/etc/bind/named.conf",
                    f"/backup/bind/named.conf.{timestamp}",
                ]
            )
        except FileNotFoundError:
            pass
        except Exception as e:
            raise Exception(f"Failed to backup BIND config: {e}")

        with open("/etc/bind/named.conf", "w") as f:
            f.write(config_str)

    def generate_zone_files(self):
        """Generate zone files for each zone based on records."""
        db = DatabaseProvider()
        zones = db.query(Zone).all()
        records = db.query(Record).all()

        for zone in zones:
            zone_records = [record for record in records if record.zone_id == zone.id]
            zone_file_str = f"; Auto-generated zone file for {zone.name}\n"
            for record in zone_records:
                zone_file_str += (
                    f"{record.name} {record.ttl} IN {record.type} {record.value}\n"
                )

            with open(f"/etc/bind/db.{zone.name}", "w") as f:
                f.write(zone_file_str)

    def update_bind_server(self):
        """Update BIND server configuration from database and reload."""
        db = DatabaseProvider()
        zones = db.query(Zone).all()
        records = db.query(Record).all()

        self.generate_bind_config(zones, records)
        self.generate_zone_files()
        self.reload_bind_server()

    async def start(self):
        """Start BIND server."""

        # try:
        #     db = DatabaseProvider()
        #     zones = db.query(Zone).all()
        #     records = db.query(Record).all()
        #     self.generate_bind_config(zones, records)
        # except Exception as e:
        #     raise Exception(f"Failed to generate BIND config: {e}")

        start_bind_command = ["rdnc", "start"]
        try:
            subprocess.run(start_bind_command, shell=True, check=True)
            print("BIND server started successfully.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to start BIND server: {e}")

    def reload_bind_server(self):
        """Reload BIND server from configuration."""
        try:
            subprocess.run(["rndc", "reload"], check=True)
        except subprocess.CalledProcessError:
            print("Failed to reload BIND server")


def get_bind_service():
    return BindService.get_instance()
