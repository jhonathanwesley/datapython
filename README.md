# datapython
Projetos e Estudos em Python para Ciência de Dados

{
    "name": "Python Dev Container",
    "image": "mcr.microsoft.com/devcontainers/python:3",
    "features": {
        "ghcr.io/devcontainers/features/python:1": {
            "version": "3.10"
        }
    },
    "settings": {
        "python.pythonPath": "/usr/local/bin/python3"
    },
    "postCreateCommand": "pip install -r requirements.txt",
    "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter"
    ]
}