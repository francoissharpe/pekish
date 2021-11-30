from fastapi.testclient import TestClient
import pytest

from pekish.app import create_app


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(create_app())
