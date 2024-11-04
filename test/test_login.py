import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app  # Import the main FastAPI app

client = TestClient(app)

def test_login_success():
    # Exemplo para teste
    test_data = {
        "email": "teste@testea",
        "senha": "testando"
    }

    # Make a POST request to the login endpoint
    response = client.post("/login/", json=test_data)

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that the response contains a token
    response_data = response.json()
    assert "token" in response_data
    assert isinstance(response_data["token"], str)

def test_login_failure():
    # Test with invalid credentials
    test_data = {
        "email": "teste@testea",
        "senha": "testando_errado"
    }

    # Make a POST request to the login endpoint
    response = client.post("/login/", json=test_data)

    # Assert that the response status code is 401 for unauthorized access
    assert response.status_code == 401
    assert response.json() == {"detail": "Usuário ou senha incorretos"}
