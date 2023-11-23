# River-Rodeo
## Lancer le back(Windows)
1. Clôner le projet
2. se placer à la racine du projet
3. Créer l'env virtuel python(que la première fois)
    ```
        python -m venv env
    ```
4. Lancer l'env virtuel
    ````
    source env/Scripts/activate
    ````
3. aller dans le répertoire server
4. lancer le back(Windows)

    ```
    pip install -r requirements.txt
    flask run --port=5001 --debug
    ```
## Lancer le front(Windows)
1. aller dans le répertoire client
2. lancer le front(Windows)
```
cd client
npm install
npm run dev
```

## Dev
### installer une nouvelle bibliothèque python(Ex de Flask)
```
pip install Flask
pip freeze -l > requirements.txt
```