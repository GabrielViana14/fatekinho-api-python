import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app  # Import the main FastAPI app
from config.config import SECRET_KEY
from config.auth import gerar_token
from datetime import datetime, timedelta
import pytz
from jose import jwt
from fastapi import APIRouter, HTTPException, Depends

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
    data = response.json()

    # Assert that the response contains a token
    response_data = response.json()
    assert "token" in response_data
    assert isinstance(response_data["token"], str)
    assert data["token_type"] == "bearer"

    # Salva o token gerado para testes subsequentes
    return data["token"]

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

def test_cont_protegido():
    login_token = test_login_success()

    # Faça uma requisição GET para a rota protegida
    response = client.get("/protegido", headers={"Authorization": f"Bearer {login_token}"})
    
    assert response.status_code == 200
    data = response.json()
    assert data["mensagem"] == "Você está autenticado!"
    assert data["usuario"]["sub"] == "teste@testea"  # O nome de usuário deve ser o mesmo do login

# Teste com token expirado
def test_token_expirado():
    # Cria um token com tempo de expiração muito curto
    data_usuario = {"sub": "teste@testea"}
    token_expirado = gerar_token(data_usuario)
    
    # Simula a expiração do token (coloca o tempo de expiração no passado)
    exp = datetime.now(pytz.utc) - timedelta(minutes=1)
    token_expirado = jwt.encode({"sub": "teste@testea", "exp": exp}, SECRET_KEY, algorithm="HS256")
    
    # Tenta acessar a rota protegida com o token expirado
    response = client.get("/protegido", headers={"Authorization": f"Bearer {token_expirado}"})
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Token expirado"
