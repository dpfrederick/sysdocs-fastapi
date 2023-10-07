from unittest.mock import patch

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


@patch("ZoneRecordService.create_zone")
def test_create_zone(mock_create_zone):
    mock_create_zone.return_value = {"id": 1, "name": "test_zone"}
    response = client.post("/zone/", json={"name": "test_zone"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "test_zone"}


@patch("ZoneRecordService.create_record")
def test_create_record(mock_create_record):
    mock_create_record.return_value = {"id": 1, "name": "test_record"}
    response = client.post("/record/", json={"name": "test_record"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "test_record"}
