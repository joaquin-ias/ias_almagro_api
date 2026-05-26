import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.main import app

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_crear_usuario():
    client = app.test_client()
    response = client.post('/usuarios', json={"nombre": "Juan"})
    assert response.status_code == 201
    assert response.get_json()["nombre"] == "Juan"