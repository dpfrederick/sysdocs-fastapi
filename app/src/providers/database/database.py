import psycopg2

from ...models import Record, Zone


class DatabaseProvider:
    def connect(self, config):
        return psycopg2.connect(
            host=config.db_host,
            port=config.db_port,
            dbname=config.db_name,
            user=config.db_user,
            password=config.db_password,
        )

    def insert_zone(self, zone: Zone):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO zones (name, version) VALUES (%s, %s) RETURNING id;",
            (zone.name, zone.version),
        )
        zone.id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

    def insert_record(self, record: Record):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO records (zone_id, type, value, version) VALUES (%s, %s, %s, %s) RETURNING id;",
            (record.zone_id, record.type, record.value, record.version),
        )
        record.id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
