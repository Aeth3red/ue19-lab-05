# ue19-lab-05 - Afficheur de Blagues

Ce projet est une simple application Python qui interroge l'API [JokesAPI](https://jokeapi.dev/) pour afficher une blague de programmation.

L'application est conçue pour être exécutée à la fois localement ou via un conteneur Docker.

---

## Fonctionnalités

* Interroge l'API `v2.jokeapi.dev` pour une blague "safe-mode".
* Affiche les blagues en une partie (single) ou en deux parties (setup/delivery).
* Gère les erreurs de connexion et de l'API.

---

## Installation et Lancement (Local)

### 1. Prérequis

* Python 3.8+
* pip

### 2. Installation

1.  Clonez ce repository :
    ```bash
    git clone [https://github.com/VOTRE-NOM/ue19-lab-05.git](https://github.com/VOTRE-NOM/ue19-lab-05.git)
    cd ue19-lab-05
    ```
2.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

### 3. Lancement

```bash
python app.py
