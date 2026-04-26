#!/bin/bash
set -e

PORT=${PORT:-5003}
echo "=== Starting Stock Prediction App ==="
echo "PORT env var: $PORT"
echo "Python version: $(python --version)"
echo "Gunicorn version: $(gunicorn --version)"
echo "Binding to 0.0.0.0:$PORT"
echo "====================================="

exec gunicorn -b "0.0.0.0:$PORT" app:app

