# Usar uma imagem base oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . /app

# Instalar as dependências do sistema (como libssl-dev)
RUN apt-get update && apt-get install -y \
    libssl-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar as dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta em que o FastAPI será executado
EXPOSE 8000

# Definir o comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
