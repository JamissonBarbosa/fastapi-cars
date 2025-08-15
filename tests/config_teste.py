# test_app.py
from fastapi.testclient import TestClient
import pytest
from fast_car_api.app import app  

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as client:
      yield client