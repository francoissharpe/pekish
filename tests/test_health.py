"""Health endpoint tests."""
from fastapi.testclient import TestClient


def test_health_ping(client: TestClient):
    """Test health ping.

    Args:
        client (TestClient): The test client.
    """
    response = client.get("/health/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}
