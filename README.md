# River-Rodeo
Projet Vue écchafauder avec vite:

√ Project name: ... river-rodeo
√ Add TypeScript? ... Yes
√ Add JSX Support? ... Yes
√ Add Vue Router for Single Page Application development? ... Yes
√ Add Pinia for state management? ... Yes
√ Add Vitest for Unit Testing? ... Yes

pas de solution de  testing bout en bout :

-  Cypress
- Nightwatch
- Playwright

Eslint  &  Prettier


## Prérequis à installer en local:
- python 12

    - Windows: Microsoft store

    - installer venv pour utiliser env virtuel  python

- Gestionnaire de version NodeJS nvm

    - Windows:  https://github.com/coreybutler/nvm-windows#installation--upgrades

    - installer nodeJS lts : 20.11.1

            nvm install lts
            nvm use lts

- Mysql
## Procédure d'initialisation du projet pour dev local (Windows)
1. Clôner le projet

        git clone [url du repo distant]

2. se placer à la racine du projet

        cd River-Rodeo/

3. Créer l'env virtuel python  12 (que la première fois)

        python3.12 -m venv env


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
    python manage.py migrate
    python manage.py runserver
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





# river-rodeo

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
    1) Run `Extensions: Show Built-in Extensions` from VSCode's command palette
    2) Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
2. Reload the VSCode window by running `Developer: Reload Window` from the command palette.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```


