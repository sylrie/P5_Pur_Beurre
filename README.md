> PROJET 5 OpenClassrooms - Substiute product - Pur Beurre

<p align="center">
    <img width=100% src="https://github.com/sylrie/P5_Pur_Beurre/blob/master/img/openfoodfacts.png">
</p>

The goal of *Pur Beurre* is to create a program that interacts with the Open Food Facts database for compare food and propose a healthier substitute for the food.

## Description

On terminal, the user receive multiple choice:
* 1-What food do you want to replace ?
* 2-Find my substituted fodds.

If the user **return 1**,
the application offers the following questions to the user:

* Select the category. [Several propositions associated with a number. The user return the number corresponding and press enter]
* Select the food. [Several propositions associated with a number. The user return the number corresponding to the chosen food and press enter]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* The application offers a substitute, its description, a store where buy it and a link to the page Open Food Facts about this food
* The user has the possibility to save the result in the database.

If the user **return 2**,
the application offers the results saved in database.

## Features

* Search for food in the Open Food Facts database.
* Le programme propose substitut, description, magasin ou l'acheter et un lien vers la page d'Open Food Facts.
* Interaction of the user with the program in the terminal.
* Management of user input errors.
* Using a MySql database.