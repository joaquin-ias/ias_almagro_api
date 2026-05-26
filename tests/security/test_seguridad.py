import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.main import app

def test_usuario_no_encontrado():
    client = app.test_client()
    response = client.get('/usuarios/99999')
    assert response.status_code == 404

def test_crear_usuario_sin_nombre():
    client = app.test_client()
    response = client.post('/usuarios', json={})
    assert response.status_code == 400