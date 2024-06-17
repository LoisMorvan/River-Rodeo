# River-Rodeo

Projet Vue écchafauder avec vite:

√ Project name: ... river-rodeo
√ Add TypeScript? ... Yes
√ Add JSX Support? ... Yes
√ Add Vue Router for Single Page Application development? ... Yes
√ Add Pinia for state management? ... Yes
√ Add Vitest for Unit Testing? ... Yes

Pas de solution de testing bout en bout :

- Cypress
- Nightwatch
- Playwright

Eslint & Prettier

## Prérequis à installer en local:

- Python 12

  - Windows: Microsoft store

  - Installer venv pour utiliser env virtuel python

- Gestionnaire de version NodeJS nvm

  - Windows: https://github.com/coreybutler/nvm-windows#installation--upgrades

  - installer nodeJS lts : 20.11.1

          nvm install lts
          nvm use lts

- Mysql

## Procédure d'initialisation du projet pour dev local (Windows)

1.  Clôner le projet

        git clone [url du repo distant]

2.  Se placer à la racine du projet

        cd River-Rodeo/

3.  Créer l'env virtuel python 12 (que la première fois)

        python3.12 -m venv env

4.  Lancer l'env virtuel
    ```
    .\env\Scripts\activate
    ```

## Lancer le back (Windows)

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

## Lancer le front (Windows)

    npm install
    npm run dev

## MySQL

### Installation de Mysql (Windows)

Allez sur ce lien https://dev.mysql.com/downloads/installer/ et télécharger la dernière version de Mysql

### Lancement de MySQL (Windows)

Si MySQL ne se lance pas au démarrage de l'ordinateur suivez cette DOC.

1. Lancer le CMD en tant qu'administrateur et lancer mysql
   ```
   net start nom_du_servie
   ```
2. Remplacer le nom du service par le nom du service que vous avez défini lors de l'installation

Par défaut pour MySQL 8.0, le nom du service est : MySQL80

### Création base de données

1. Créer une BDD riverroder

```
CREATE DATABASE riverrodeo;
```

2. Créer un utilisateur sur le localhost username(Ex: adminRiverRoder) avec tous les droits sur le shéma & conserver le mdp

```
CREATE USER 'adminRiverRoder'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON riverrodeo . * TO 'adminRiverRoder'@'localhost';
```

## Ajout des variables d'environnements

1. Créer les fichier d'environnement
   ```
   touch .env
   ```
2. Dans le fichier .env ajouter les varaibles d'environnement nécéssaire

   ```
    DJANGO_ENV=environnement
    DATABASE_NAME=database_name
    DATABASE_USER=database_user
    DATABASE_PASSWORD=database_password
    DATABASE_PORT=database_port
    SECRET_KEY="secret_key"
   ```

   Remplacer la variable "environnement" par votre environnement -> "development" ou "production".

   Remplacer les variables "database_name", "database_user", "database_password" par les informations de votre base de données.

   Remplacer la variable "secret_key" par la secret key de votre projet.

   Remplacer la variable "database_port" par le port du service mysql (3306 par défaut)

## Dev

### Installation d'une nouvelle bibliothèque Python (Ex de Flask)

- Une foi dans le répertoire serveur

```
pip install Flask
pip freeze -l > requirements.txt
```

### Création super utilisateur Django

```
python manage.py createsuperuser
```

# river-rodeo

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
   1. Run `Extensions: Show Built-in Extensions` from VSCode's command palette
   2. Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
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
