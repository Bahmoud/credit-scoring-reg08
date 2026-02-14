# Dockerfile pour l'API de Credit Scoring

FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY src/ ./src/
COPY api/ ./api/
COPY models/ ./models/

# Exposer le port de l'API
EXPOSE 8000

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/')"

# Commande de lancement
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
