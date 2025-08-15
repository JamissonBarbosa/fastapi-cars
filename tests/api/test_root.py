from fastapi.testclient import TestClient
from fast_car_api.app import app  # Importe sua aplicação FastAPI

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}