from fastapi.testclient import TestClient


def test_health_ping(client: TestClient):
    response = client.get("/health/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


# def test_health_report(client: TestClient):
#     response = client.get("/health/report")
#     assert response.status_code == 200
#     assert response.json() == {"message": "ok"}
