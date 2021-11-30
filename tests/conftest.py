"""Shared pytest fixtures."""
from fastapi.testclient import TestClient
import pytest

from pekish.app import create_app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Client fixture.

    Returns:
        TestClient: The test client
    """
    return TestClient(create_app())
