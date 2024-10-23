# Utilisez une image Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de configuration de l'application
COPY pyproject.toml poetry.lock ./

# Installer Poetry
RUN pip install poetry

# Installer les dépendances sans créer un environnement virtuel
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copier tous les fichiers de l'application
COPY . .

# Exposer le port utilisé par l'application FastAPI
EXPOSE 8000

# Commande pour lancer l'application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
