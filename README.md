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

   Une fois le serveur démarré, accédez à l'API à l'adresse suivante :

   ```
   http://127.0.0.1:8000/docs
   ```

   Cela vous donnera accès à l'interface Swagger pour interagir avec les différents points de terminaison de l'API.

## Fonctionnalités

- Système d'enregistrement et d'authentification des utilisateurs avec protection JWT.
- Intégration de données vocales sous forme de tableau de coordonnées vocales.
- Routes protégées par JWT pour accéder aux informations utilisateur.

## Participants

- Abdou Samath Seck
- Dorian Lovichi
- Dahdouh Ahmed

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Fork le projet.
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Effectuez vos modifications et validez-les (`git commit -m 'Add some AmazingFeature'`).
4. Poussez votre branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

