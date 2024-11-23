import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app
import pytz
from jose import jwt
from fastapi import APIRouter, HTTPException, Depends

client = TestClient(app)

@pytest.fixture
def create_usuario():
    # Dados para criar o usuário
    test_data = {
        "email": "teste@alterar",
        "senha": "apagar",
        "tipo": "teste"
    }
    # Cria o usuário
    response = client.post("/usuarios/", json=test_data)
    assert response.status_code == 200  # Verifica se a criação foi bem-sucedida
    user_id = response.json().get("idUsuario")  # Obtém o ID do usuário criado

    # Yield permite que o teste use o ID do usuário
    yield user_id

    # Após o teste, exclui o usuário criado
    response = client.delete(f"/usuarios/{user_id}")
    assert response.status_code == 200  # Verifica se a exclusão foi bem-sucedida


def test_create_usuario(create_usuario):
    user_id = create_usuario
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 200  # Verifica se o usuário foi criado e pode ser obtido
    assert response.json()["idUsuario"] == user_id  # Verifica se o ID corresponde ao esperado


def test_update_usuario(create_usuario):
    user_id = create_usuario
    test_data = {
        "email": "teste@alterar@nova.com",
        "senha": "nova_senha",
        "tipo": "admin"
    }
    
    # Atualiza o usuário
    response = client.put(f"/usuarios/{user_id}", json=test_data)
    assert response.status_code == 200  # Verifica se a atualização foi bem-sucedida

    # Verifica se a atualização foi aplicada
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == test_data["email"]  # Verifica se o email foi atualizado


def test_get_usuario(create_usuario):
    user_id = create_usuario
    # Verifica se o usuário pode ser recuperado corretamente
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 200
    assert response.json()["idUsuario"] == user_id  # Verifica se o ID corresponde ao esperado


def test_delete_usuario(create_usuario):
    user_id = create_usuario
    # Exclui o usuário
    response = client.delete(f"/usuarios/{user_id}")
    assert response.status_code == 200  # Verifica se a exclusão foi bem-sucedida

    # Verifica se o usuário foi realmente excluído
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 404