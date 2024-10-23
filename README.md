
# VoiceDetector

## Description
L'objectif de ce projet est de développer une intelligence artificielle (IA) capable d'identifier une voix et de l'associer à un utilisateur précis. Ce système pourrait être utilisé dans divers cas d'utilisation tels que l'authentification sécurisée, la reconnaissance d'utilisateurs dans des applications vocales ou encore la personnalisation d'interactions en fonction des utilisateurs.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Python](https://www.python.org/downloads/) (version 3.9 ou supérieure)
- [Poetry](https://python-poetry.org/docs/#installation) pour la gestion des dépendances

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd voicedetector
   ```

2. Créez la base de données PostgreSQL et définissez les informations de connexion (comme l'hôte, le port, le nom d'utilisateur, le mot de passe et le nom de la base de données) dans le fichier `.env` sous forme de variables d'environnement.

3. Installez les dépendances avec Poetry :

   ```bash
   poetry install
   ```

4. Lancez le projet FastAPI :

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Remplacez `main:app` par le chemin du fichier contenant l'instance de l'application FastAPI si nécessaire.

## Configuration

1. **Variables d'environnement :**
   Assurez-vous d'avoir un fichier `.env` contenant les variables d'environnement suivantes :

   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=voicedetector_db_for_example
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

   Modifiez ces valeurs selon votre configuration.

2. **Base de données :**
   PostgreSQL est utilisé pour stocker les données de l'application. Veillez à ce que votre base de données soit configurée et accessible avec les variables d'environnement spécifiées.

## Utilisation

- **Démarrer le serveur :** Utilisez la commande suivante pour démarrer le serveur :

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Remplacez `main:app` par le chemin du fichier contenant l'application FastAPI.

- **Accéder à l'API :** Une fois le serveur démarré, accédez à l'API via `http://localhost:8000` ou l'URL indiquée par Uvicorn.
