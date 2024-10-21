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

2. Installez les dépendances avec Poetry :

   ```bash
   poetry install
   ```

## Configuration

1. **Base de données :**
   Configurez votre base de données dans le fichier de configuration approprié (par exemple, `config.py` ou `settings.py`). Assurez-vous d'installer les pilotes nécessaires, comme `psycopg2` pour PostgreSQL.

2. **Variables d'environnement :**
   Créez un fichier `.env` pour définir vos variables d'environnement, comme les informations d'authentification pour la base de données.

## Utilisation

1. **Démarrer le serveur :**

   Utilisez la commande suivante pour démarrer le serveur :

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Remplacez `main:app` par le nom de votre fichier principal si nécessaire.

2. **Accéder à l'API :**

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
