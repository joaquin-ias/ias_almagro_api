import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.main import app

def test_flujo_completo():
    client = app.test_client()

    res = client.post('/usuarios', json={"nombre": "Maria"})
    assert res.status_code == 201
    user_id = res.get_json()["id"]

    res = client.get(f'/usuarios/{user_id}')
    assert res.status_code == 200
    assert res.get_json()["nombre"] == "Maria"

    res = client.delete(f'/usuarios/{user_id}')
    assert res.status_code == 200

    res = client.get(f'/usuarios/{user_id}')
    assert res.status_code == 404