# imagin

Ce site a été réalisé dans le cadre d’un projet de ma formation à Télécom SudParis. L’objectif était d’imaginer des solutions innovantes pour répondre à des problématiques rencontrées par la ville d’Évry-Courcouronnes.

Le projet vise à explorer et proposer des idées pour améliorer la vie urbaine, en s’appuyant sur l’analyse des besoins locaux et la créativité des étudiants.

---

## Documentation

### Présentation du site

Le site **imagin** propose une plateforme interactive permettant aux utilisateurs de découvrir et de soumettre des idées innovantes pour améliorer la ville d’Évry-Courcouronnes. Il met en avant la collaboration citoyenne et l’innovation urbaine.

### Fonctionnalités principales

- **Accueil** : Présentation du projet et des objectifs.
- **Idées** : Liste des idées proposées, avec possibilité de filtrer par catégorie.
- **Soumission d’idées** : Formulaire permettant aux utilisateurs de proposer leurs propres solutions.
- **Vote et commentaires** : Les utilisateurs peuvent voter et commenter les idées.
- **Statistiques** : Visualisation des tendances et des idées les plus populaires.


### Installation avec Docker

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/EvanescentApps/imagin-site
    ```
    
2. Construisez l’image Docker :
    ```bash
    cd imagin
    docker build -t imagin-site .
    ```

3. Lancez le conteneur :
    ```bash
    docker run -p 3000:3000 imagin-site
    ```

Le site sera accessible sur [http://localhost:3000](http://localhost:3000)

### Structure du projet

- `src/` : Contient le code source du site.
  - `components/` : Composants réutilisables.
  - `pages/` : Pages principales du site.
  - `assets/` : Images et fichiers statiques.
- `public/` : Fichiers accessibles publiquement.
- `README.md` : Documentation du projet.
