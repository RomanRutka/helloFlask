# helloFlask
*Dépôt pour l'étude de cas 3 (projet orienté objet)*  
  
## Installation et utilisation de Pyenv :

### Installation :
- Installer les dépendances :
```
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

- Installer Pyenv : `$ curl https://pyenv.run | bash`

- Dans le ficher `.bashhrc`, ajouter les lignes suivantes :
```
# Load pyenv automatically
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Load pyenv-virtualenv automatically
eval "$(pyenv virtualenv-init -)"
```

- Toujours dans le fichier `.bashhrc`, commenter les lignes entre `>>> conda initialize >>>` et `# <<< conda initialize <<<`


### Utilisation :

- `pyenv` pour avoir une liste de toutes les commandes possibles avec pyenv, et leur description

- `pyenv versions` donne les versions installées / accessibles sur la machine
- `pyenv install --list` montre toutes les versions de python installables
- `pyenv install [VERSION NAME]` pour installer la version précisée
- `pyenv activate NOM` active l'environnement / la version précisée
- `pyenv virtualenv PYTHONVERSION ENVIRNAME` pour créer un environnement dans la version voulue, et lui donner le nom mentionné 
- `pyenv global NUMVERSION` pour préciser la verison de python pour l'interpréteur global de la machine
- `pyenv local NUMVERSION` pour préciser la version de python utilisée dans le répertoire où on se trouve (i.e. pour un projet donné)


## Installation et utilisation de poetry :
### Installation :
- `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -` (peut nécessité un redémarrage du pc)

### Utilisation :
- Pour vérifier que poetry est bien installé : `poetry --version` 
- Créer un nouveau projet : `poetry new PROJECTNAME` 
- Ajouter un package aux dépendances : `poetry add PACKAGENAME` exemple : `poetry add pandas`
- Installer l'appli : `poetry install`
- Utiliser l'appli (après installation) : `poetry run APPLICATIONNAME`
- LE PLUS IMPORTANT : créer un fichier .whl avec toutes les dépendances : `poetry build`. Crée un dossier ./dist dans lequel se trouve le .whl
- après au moins 1 `poetry install`, la ligne `poetry shell` permet de se mettre dans l'environnement virtuel créé automatiquement par poetry 
