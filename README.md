# Hybrid-Car-Rental
Cette application Desktop permet aux administrateurs de gérer leur flotte de voitures disponibles à la location ainsi que leur personnel, et aux employés de traiter les demandes de location des clients.
## Technologies
 - Python
 - Tkinter 
 - sqlite

## Configuration Base de Données
Pour configurer la base de données :

 - Ouvrez le fichier login.py.
 - Vérifiez que les informations de la base de données correspondent à celles de votre machine.
 - Exécutez le script pour créer la base de données en utilisant la commande suivante : python login.py 

## Utilisation

- Pour accéder à l'application, vous devez exécuter le fichier login.py. Vous pouvez ensuite vous connecter en utilisant votre nom d'utilisateur et votre mot de passe.

- Si vous êtes un client, vous pouvez utiliser l'application pour rechercher et réserver des voitures disponibles à la location. Vous pouvez également afficher les informations détaillées des voitures, telles que les images et les caractéristiques, avant de les réserver.

- Si vous êtes un administrateur, vous devez vous connecter avec les identifiants suivants : username "admin" et mot de passe "123". En tant qu'administrateur, vous pouvez gérer les voitures disponibles à la location. Vous pouvez ajouter de nouvelles voitures à la liste et supprimer celles qui ne sont plus disponibles. 

-N'oubliez pas de vous déconnecter de votre session en cliquant sur le bouton "LOGOUT" une fois que vous avez terminé d'utiliser l'application.

## Fonctionnalités

- Authentification et autorisation : l'application dispose d'un système de login pour gérer les accès aux différentes fonctionnalités de l'application. Les utilisateurs doivent s'authentifier pour accéder à leur compte.
- Gestion des admin : les fichier addCar.py et DeletCar.py et FacturesList.py permet aux utilisateurs d'ajouter, supprimer et afficher liste des factures des voitures .
- Gestion des clients : le fichier Booking.py , SearchCar.py , carList.py permet aux utilisateurs reserver, afficher la list des voiture.
- LogOut : l'application dispose d'une fonctionnalité de déconnexion qui permet aux utilisateurs de se déconnecter de leur compte

## screenshots
- login
![login](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/4adbd354-9e7c-493b-a877-5dcd5bbb65dd)
- sign up
![singnup](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/ce8fd4a3-e8db-4f4b-8ec8-261868238834)
### partie admin
- admin menu
![admin-menu](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/6e6ddde3-526d-48be-a58a-14da408a7afe)
- ajouter voiture

![add-rolls-car-1](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/2b9382c5-483b-4410-a1cb-1fda5a918d0a)
- supprimer voiture
![deletecar](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/b334c4d5-eb24-4512-913b-1f9567159392)
- afficheages les list des factures
![factures-1](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/c5ba476a-8dd2-42c6-a5b1-0d64ed35d3e2)

### partie client
- client menu
![menu-user](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/8261ea0f-2b85-4581-903e-d9a4dbf39c65)
- affichage des voitures
![carlist](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/418326ca-2588-46c4-9c53-2ce7f4548e12)
- recherche 
![search-rolls-car](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/d035a326-926c-425f-815f-e7f48026c53f)
- reserver voiture
![book-car](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/5b66970e-0c77-4dd2-9b2d-0440d0b9a2bd)

- log out 
![logout-admin](https://github.com/yassine355/Hybrid-Car-Rental/assets/72927054/a0865673-98b9-43d2-8bd1-bb9e6cc8b780)

