# River-Rodeo
## Lancer le back (Windows)
1. Clôner le projet
2. se placer à la racine du projet
3. Créer l'env virtuel python (que la première fois)
    ```
    python -m venv env
    ```
4. Lancer l'env virtuel
    ````
    source env/Scripts/activate
    ````
3. Aller dans le répertoire server
4. Lancer le back(Windows)

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

## Dev
### Installation d'une nouvelle bibliothèque Python (Ex de Flask)
```
pip install Flask
pip freeze -l > requirements.txt
```