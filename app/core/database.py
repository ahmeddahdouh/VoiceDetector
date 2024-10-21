import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# Récupérer les variables d'environnement
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']

# Construire l'URL de connexion à la base de données
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Créer le moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

Base = declarative_base()



