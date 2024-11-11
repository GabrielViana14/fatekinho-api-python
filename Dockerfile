FROM python:3.11-slim

# Instalar dependências do sistema e o Rust
RUN apt-get update && apt-get install -y \
    libssl-dev \
    gcc \
    python3-dev \
    curl \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && . $HOME/.cargo/env \
    && rm -rf /var/lib/apt/lists/*  # Limpar o cache dos pacotes APT

# Instalar as dependências do Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o código da aplicação
COPY . /app
WORKDIR /app

# Expor a porta em que o FastAPI será executado
EXPOSE 8000

# Rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
