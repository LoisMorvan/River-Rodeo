# River-Rodeo

## Lancer le back (Windows)

1. Clôner le projet
2. se placer à la racine du projet
3. Créer l'env virtuel python (que la première fois)
   ```
   python -m venv env
   ```
4. Lancer l'env virtuel
   ```
   source env/Scripts/activate
   ```
5. Aller dans le répertoire server
6. Lancer le back(Windows)

   ```
   pip install -r requirements.txt
   flask run --port=5001 --debug
   ```

## Lancer le front (Windows)

1. Aller dans le répertoire client
2. Lancer le front (Windows)
   ```
   cd client
   npm install
   npm run dev
   ```

## Installation de Mysql (Windows)

Allez sur ce lien https://dev.mysql.com/downloads/installer/ et télécharger la dernière version de Mysql

## Ajout des variables d'environnements

1. Aller dans le répertoire server
2. Créer les fichier d'environnement
   ```
   cd server
   mkdir instance
   touch .env
   cd instance
   touch config.py
   ```
3. Dans le fichier .env ajouter les varaibles d'environnement nécéssaire

   ```
   FLASK_ENV=environnement
   DEV_DATABASE_URI=your_prod_database_uri
   PROD_DATABASE_URI=your_prod_database_uri
   ```

   Remplacer la varaible "environnement" par votre environnement -> "development" ou "production"
   Remplacer les variables "your_prod_database_uri" par les URL des base de données -> mysql://root:password@localhost:3306/mydatabase

4. Dans le fichier config.py ajouter le texte suivant

   ```
   import os

   class Config:
       SQLALCHEMY_TRACK_MODIFICATIONS = False

   class DevelopmentConfig(Config):
       SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

   class ProductionConfig(Config):
       SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
   ```

## Dev

### Installation d'une nouvelle bibliothèque Python (Ex de Flask)

```
pip install Flask
pip freeze -l > requirements.txt
```
