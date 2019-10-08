# PROJET 5 OC
# Utilisation d'Open food Facts

Rieutor sylvain

L'idée de **Pur Beurre** est de créer un programme interagissant avec la base Open Food Facts.
Ce programme permet de récupérer les aliments de la base de donnée d'Open Food Facts, les comparer et proposer é l'utilisateur un substitut plus sain é l'aliment qui lui fait envie.

## Description

Sur le terminal, l'utilisateur se voit proposer plusieurs choix :
* 1-Quel aliment souhaitez-vous remplacer ?
* 2-Retrouver les aliments substitués.

Si l'utilisateur **sélectionne 1**. Le programme pose les questions suivantes é l'utilisateur et ce dernier sélectionne les réponses :
* Sélectionnez la catégorie. [Plusieurs propositions associées é un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées é un chiffre. L'utilisateur entre le chiffre correspondant é l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

Si l'utilisateur **sélectionne 2**, le programme affiche le résultat des recherchez déjé effectués permettant ainsi d'éviter de refaire une recherche dans la base de donnée.

## Fonctionnalités

* Recherche d'aliments dans la base Open Food Facts.
* Le programme propose substitut, description, magasin ou l'acheter et un lien vers la page d'Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal (potentiellement une interface graphique).
* Si l'utilisateur entre un caractére qui n'est pas un chiffre, le programme lui répéte la question.
* La recherche s'effectue sur une base MySQL.