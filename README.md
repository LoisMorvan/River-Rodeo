# River-Rodeo
## Lancer le back(Windows)
1. Clôner le projet
2. se placer à la racine du projet
3. lancer le back(Windows)
    ```
    python3.12 -m venv env
    source env/Scripts/activate
    pip install -r requirements.txt
    flask run --port=5001 --debug
    ```
## Lancer le front(Windows)
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