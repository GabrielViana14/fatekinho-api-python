from fastapi import FastAPI
from rotas.clientes import router as clientes_router
from rotas.usuarios import router as usuarios_router
from rotas.autenticacao import router as auth_router

# Rodar a API localmente: uvicorn main:app --reload
# Rodar a API no github Codespace: uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Para testar API só usar a url: http://127.0.0.1:8000/docs
# caso esteja em outra url é só adicionar o /docs no final da url

app = FastAPI()
app.include_router(clientes_router)
app.include_router(usuarios_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return "API rodando"