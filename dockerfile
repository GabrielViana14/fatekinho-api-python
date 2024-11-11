# Usando uma imagem base Python
FROM python:3.9-slim

# Instalar dependências de build do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libssl-dev \
    libffi-dev

# Instalar Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Adicionar maturin
RUN pip install maturin

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos para dentro do contêiner
COPY . /app

# Instalar as dependências Python
RUN pip install -r requirements.txt

# Expôr a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
