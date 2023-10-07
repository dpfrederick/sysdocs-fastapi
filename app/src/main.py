import uvicorn
from fastapi import Depends, FastAPI

from .config import Config, get_config
from .models import Record, Zone
from .providers.database import DatabaseProvider
from .services.audit import AuditService
from .services.bind import BindService

app = FastAPI(
    title="Sysdocs rewrite with FastAPI",
    description="Administration API for sysdocs rewrite. Generate DNS records.",
)


@app.on_event("startup")
async def startup_event():
    bind = BindService()
    await bind.start()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/app_name")
def read_settings(settings: Config = Depends(get_config)):
    return settings.app_name


@app.post("/zone/")
def create_zone(zone: Zone):
    db = DatabaseProvider()
    audit = AuditService()
    bind = BindService()
    zone.version = 1
    db.insert_zone(zone)
    audit.log("zone_create", str(zone))
    bind.update_bind_server()
    return zone


@app.post("/record/")
def create_record(record: Record):
    db = DatabaseProvider()
    audit = AuditService()
    bind = BindService()
    record.version = 1
    db.insert_record(record)
    audit.log("record_create", str(record))
    bind.update_bind_server()
    return record


if __name__ == "__main__":
    print("Swagger page launched at http://127.0.0.1:8080/docs")
    uvicorn.run(app, host="127.0.0.1", port=8080)
