# Grainotheque

## Préambule
Vous recherchez une semence particulière, vous disposez d'une graine, vous souhaitez connaitre les particuliarités de culture d'une espèce, vous pouvez consulter notre base de données et venir chercher votre bonheur directement à la Quincaillerie de Guéret ou à la Bibiothèque Multimédia Intercommunale.

## Démo
Accéder à la démo(en cours de développement)

## Installation en local (Linux)

Récupération des sources en local

* `git clone https://github.com/martinsam/graino:xw:.git`

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

Il faud maintenant importer les données dans la base

* 'python manage.py loaddata fixtures/categories.json'

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

## Fonctionalitées : 
* Actuellement le projet est capable de gérer des catégories de graines en cascade, et d'associer à chacune de ces catégories un ensemble de variétées.
* Il est possible de se créer un compte, et de le gérer.
 - Possibilitée de modifier ses informations personelle (Nom, Prénom, Adresse).
 - Possibilitée d'ajouter des variétées et/ou des catégories à celles déjà référencées.
 - Possibilitée de tenir un inventaire et une liste demandes.
 - Possibilitée de créer et/ou d'être invité à rejoindre un groupe.
 - Possibilité d'ajouter et/ou supprimer des variétées aux inventaires des groupes aux quelles on appartiens.
* Géolocalisation des groupes (Grainothèques).
* Moteur de recherche des Variétées / Catégories présentes dans la base.
 - Le moteur de recherche ne gére pas encore l'autocomplésion.
