#!/bin/bash
# Script de inicialização para Railway
# Lê a variável PORT e inicia o Gunicorn

PORT=${PORT:-8080}
echo "🚀 Iniciando servidor na porta $PORT"

exec gunicorn wsgi:app --bind 0.0.0.0:$PORT
