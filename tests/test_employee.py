from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "UP"


def test_get_employees():
    response = client.get("/employees")

    assert response.status_code == 200


def test_create_employee():
    response = client.post(
        "/employees", json={"id": 2, "name": "Vamsi", "department": "Platform"}
    )

    assert response.status_code == 200
    assert response.json()["id"] == 2
