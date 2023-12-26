# River-Rodeo
## Prérequis:
- installer python
- installer nodeJS
- installer mysql
## Lancer le back (Windows)
1. Clôner le projet
2. se placer à la racine du projet
3. Créer l'env virtuel python (que la première fois)
    ```
    python -m venv env
    ```
4. Lancer l'env virtuel
    ````
    .\env\Scripts\activate
    ````
3. Aller dans le répertoire server
   ```
   cd .\server\
   ```
4. Lancer le back(Windows)

    ```
    pip install -r requirements.txt
    flask run --port=5001 --debug
    ```
## Lancer le front (Windows)
1. Aller dans le répertoire client
   ```
   cd client
   ```
2. Lancer le front (Windows)
    ```
    npm install
    npm run dev
    ```

## Installation de Mysql (Windows)
- télécharcher serveur mysql et conserver mdp root

- installer un client mysql et se connecter au serveur via mdp root
- créer une BDD(schéma) riverroder
- créer un utilisateur sur le localhost username(Ex: adminRiverRoder) avec tous les droits sur le shéma & conserver le mdp
- paramétrer le config.py avec SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'

## Dev
### Installation d'une nouvelle bibliothèque Python (Ex de Flask)

- Une foi dans le répertoire serveur
```
pip install Flask
pip freeze -l > requirements.txt
```