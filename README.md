# Grainotheque

## Préambule
Vous recherchez une semence particulière, vous disposez d'une graine, vous souhaitez connaitre les particuliarités de culture d'une espèce, vous pouvez consulter notre base de données et venir chercher votre bonheur directement à la Quincaillerie de Guéret ou à la Bibiothèque Multimédia Intercommunale.

## Démo
Accéder à la démo(en cours de développement)

## Installation en local (Linux)

Récupération des sources en local

* `git clone https://github.com/martinsam/grainotheque.git`

Installation et activation de l'environnement virtuel

* `virtualenv env --no-site-package`
* `source env/bin/activate`

Installation des paquets python nécessaires 

* `pip install --upgrade pip`
* `pip install -r requirements.txt`

Synchronisation de la base de données avec les modèles django

* `python manage.py migrate`

A ce niveau là votre base de données est vide. Il reste une dernière étape. Création d'un compte superuser

* `python manage.py createsuperuser`

Suivez la procédure dans le terminal

## Démarrer le serveur en local

Lancer le serveur sur localhost

* `python manage.py runserver`

Dans Firefox allez sur [http://localhost:8000](http://localhost:8000) pour la vue client et 
[http://localhost:8000/admin/](http://localhost:8000/admin/) pour la vue d'administration


## Déploiement en ligne (Linux)

Au préalable il est nécessaire de disposer d'un serveur Unix configuré pour supporter python 2.7 et supérieur.
Pour installer l'environnement de production vous pouvez appliquer la partie "Installation en local" directement sur
votre serveur.

Une procédure de déploiement SFTP ou FTP est prévue via l'utilitaire `dploy`. Pour ce faire il faut installer le paquet 
node de la façon suivante :

* `sudo npm install dploy`
* Renommer le fichier dploy.yaml.exemple en dploy.yaml
* Définir vos propre paramètre ftp et path dans dploy.yaml
* Lancer le déploiement avec la commande `dploy <nom_du_serveur>`. Si un seul serveur est défini la commande `dploy`
 suffit.


Pour tout détail de configuration `dploy` référez vous à la [documentation officielle](https://github.com/LeanMeanFightingMachine/dploy).
