from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.post("/predict/'")
    assert response.status_code == 200
    #assert response.json() == {"text": "Скоро наступит Новый Год!"}
