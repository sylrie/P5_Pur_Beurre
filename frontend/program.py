""" program
    Loop and action for the program
"""

#! /usr/bin/env python3
# coding: UTF-8

# programs import
import backend.functions as functions
from backend.functions import color_print
from backend.functions import check_input

from backend.manager_db import ManagerDb
from backend.manager_api import ManagerApi
import backend.tables_db as tables


class Program():
    """ Manage the program """

    def __init__(self):

        self.loop_database = ManagerDb()
        self.categories = ManagerApi().categories
        self.loop = True
        self.selected_category = ""
        self.user = ""

        self.program_loop()

    def select_user(self):
        """ select a user"""

        users = tables.show_table("users")

        color_print(
            "data",
            "Liste utilisateur(s) :"
        )

        for row in users:

            color_print(
                "data",
                "{} : {}"
                .format(
                    row[0],
                    row[1]
                    )
                )

        if not users:
            color_print(
                "normal",
                "Vous devez créer un utilisateur"
            )
            self.new_user()

        else:
            loop = False
            while not loop:

                color_print(
                    "normal",
                    "Veuillez entrer le NUMERO d'utilisateur ('+' pour nouveau)"
                )
                nbr = input()

                if nbr == "+":
                    loop = True
                    self.new_user()

                else:
                    check = check_input(nbr)

                    if check:
                        nbr = int(nbr)

                        if nbr - 1 in range(len(users)):

                            username = tables.show_value('username', 'users', 'id', nbr)
                            color_print(
                                "normal",
                                "Bienvenue {} !"
                                .format(
                                    username[0][0]
                                )
                            )
                            self.user = nbr
                            loop = True

                        else:
                            functions.not_in_list()

                    else:
                        functions.not_int()

    def new_user(self):
        """ Create a user """

        color_print(
            "normal",
            "Veuillez entrez votre nom:"
        )
        username = input()

        tables.add_user(
            username
        )

        color_print(
            "normal",
            "L'utilisateur {}, à été crée."
            .format(
                username
            )
        )

        self.select_user()

    def program_loop(self):
        """ loop for program """

        color_print(
            "normal",
            "Bonjour!"
        )

        while self.loop:

            action = self.action_choice()
            if action == 1:
                self.select_category()
                self.select_food()
            elif action == 2:
                self.show_favorites()

        color_print(
            "normal",
            "A bientôt !"
        )

    def action_choice(self):
        """ Select first action """

        loop = False
        while not loop:

            color_print(
                "data",
                "1. Quel aliment souhaitez-vous remplacer ?"
            )
            color_print(
                "data",
                "2. Retrouver mes aliments substitués."
            )
            color_print(
                "data",
                "3. Quitter"
            )
            color_print(
                "normal",
                "Entrez le NUMERO correspondant à votre choix:"
            )

            action = input()

            test = check_input(action)

            if test:
                action = int(action)
                if action in (1, 2):
                    loop = True
                    return action

                elif action == 3:
                    loop = True
                    self.loop = False

                else:
                    functions.not_in_list()

            else:
                functions.not_int()

    def select_category(self):
        """ Select a categry in Food table """

        loop = False
        while not loop:

            color_print(
                "data",
                "Affichage des catégories..."
            )

            cat = 0
            for category in self.categories:
                cat += 1
                color_print(
                    "data",
                    "{} : {}"
                    .format(
                        cat,
                        category
                    )
                )

            color_print(
                "normal",
                "Veuillez entrez le NUMERO de la catégorie: "
            )

            cat = input()

            check = check_input(cat)
            if check:

                cat = int(cat) - 1

                if cat in range(len(self.categories)):
                    loop = True
                    self.selected_category = self.categories[cat]
                else:
                    functions.not_in_list()

            else:
                functions.not_int()

    def select_food(self):
        """ select food in food list """

        color_print(
            "normal",
            "Produits de la catégorie {}:"
            .format(
                self.selected_category
            )
        )

        result = tables.show_value(
            "id, food_name, brand", "food", "category", self.selected_category
        )

        count = 1
        for food in result:

            color_print(
                "data", """{}: {} - {} -""".format(
                    count,
                    food[1],
                    food[2]
                )
            )
            count += 1

        loop = False
        while not loop:

            color_print(
                "normal",
                "Choissez un NUMERO d'aliment :"
            )
            select = input()

            check = check_input(select)
            if check:

                select = int(select)
                if select - 1 in range(len(result)):

                    id_selected = result[select - 1][0]

                    color_print(
                        "data",
                        "Vouz aves selectionné le produit:"
                    )
                    color_print(
                        "normal",
                        result[select - 1][1]
                    )

                    loop = True

                else:
                    functions.not_in_list()

            else:
                functions.not_int()

        self.substitute(id_selected)

    def substitute(self, id_selected):
        """ show possible substitutes """

        nutriscores = [
            "a",
            "b",
            "c",
            "d",
            "e"
        ]

        result = tables.show_value(
            "*",
            "food",
            "id",
            id_selected
        )

        nutrigrade = result[0][7]
        color_print(
            "normal",
            "Ce produit à pour nutrigrade: {} "
            .format(
                nutrigrade.upper()
            )
        )

        for score in nutriscores:
            substitute_nutriscore = score
            food = tables.show_mutli(
                "*",
                "food",
                (
                    "category",
                    "nutrigrade"
                ),
                (
                    self.selected_category,
                    score
                )
            )

            if nutrigrade == substitute_nutriscore:
                color_print(
                    "error",
                    "Nous n'avons pas de prodruit avec un meilleur nutrisgrade à proposer"
                )

            if len(food) > 0:
                break

        color_print(
            "normal",
            "Nous vous proposons ces poduits avec un nutrigrade de: {} "
            .format(
                substitute_nutriscore.upper()
            )
        )

        count = 1
        for product in food:
            color_print(
                "data", "{}: {}, Marque: {}, Magasins: {}".format(
                    count,
                    product[2],
                    product[4],
                    product[5]
                )
            )
            color_print(
                "link",
                "liens: {}"
                .format(
                    product[6]
                )
            )

            count += 1

        loop = False
        while not loop:

            color_print(
                "normal",
                "Souhaitez vous enregistrer un de ces subsituts dans vos favoris?"
            )

            color_print(
                "normal",
                "1. Oui\n2. Non"
            )

            action = input()

            check = check_input(action)
            if check:

                action = int(action)

                if action == 1:
                    self.save_food(food)
                    loop = True

                elif action == 2:
                    loop = True

                else:
                    functions.not_in_list()

            else:
                functions.not_int()

    def save_food(self, food_list):
        """ Add favorite """

        if self.user == "":
            self.select_user()
        else:
            pass

        if len(food_list) == 1:
            food = 0

        else:
            color_print(
                "normal",
                "entrez le NUMERO du produit à enregistrer:"
            )
            loop = False
            while not loop:

                food = input()

                check = check_input(food)
                if check:

                    food = int(food) - 1
                    if food in range(len(food_list)):
                        loop = True
                    else:
                        functions.not_in_list()

                else:
                    functions.not_int()

        message = tables.add_favorite(self.user, food_list[food][0])

        color_print(
            "normal",
            message
        )

    def show_favorites(self):
        """ Show favorite's user """

        if self.user == "":
            self.select_user()
        else:
            pass

        result = tables.show_value(
            "foodid",
            "favorites",
            "userid",
            self.user
        )

        if result:
            color_print(
                "normal",
                "Voici vos favoris:"
            )

            count = 1
            for food in result:
                favorite = tables.show_value(
                    "Category, Food_Name, Nutrigrade",
                    "Food",
                    "id",
                    food[0]
                )

                color_print(
                    "data",
                    "{}. Catégorie: {}, {}, Nutrigrade {}"
                    .format(
                        count,
                        favorite[0][0],
                        favorite[0][1],
                        favorite[0][2].upper()
                    )
                )
                count += 1

            loop = False
            while not loop:

                color_print(
                    "normal",
                    "Que souhaitez-vous faire ? "
                )

                color_print(
                    "data",
                    "1. Voir un produit. \n2. Supprimer un produit. \n3. Retourner au menu. "
                )

                action = input()

                check = check_input(action)
                if check:

                    action = int(action)

                    if action in (1, 2):
                        self.favorites_options(result, action)
                        loop = True

                    elif action == 3:
                        loop = True

                    else:
                        functions.not_in_list()

                else:
                    functions.not_int()

        else:
            color_print(
                "normal",
                "Vous n'avez pas encore enregistré de favoris"
            )

    def favorites_options(self, favorites, action):
        """ option for favorites table """

        if action in (1, 2):

            color_print(
                "data",
                "Entrez le NUMERO du produit:"
            )

            loop = False

            while not loop:

                food = input()

                check = check_input(food)
                if check:

                    food_id = favorites[int(food)-1][0]
        
                    if action == 1:
                        food = tables.show_value(
                            "*",
                            "Food",
                            "id",
                            food_id
                        )

                        color_print(
                            "normal",
                            food[0][2]
                        )

                        color_print(
                            "data",
                            """Catégorie: {}\nMarque: {}\nNutrigrade: {}\nMagasin(s): {}"""
                            .format(
                                food[0][1],
                                food[0][4],
                                food[0][7].upper(),
                                food[0][5]
                            )
                        )

                        color_print(
                            "link",
                            food[0][6]
                        )
                        color_print(
                            "normal",
                            "          ----------------------          "
                        )
                        loop = True

                    elif action == 2:
                        tables.action_values(
                            "DELETE",
                            "Favorites",
                            "FoodID",
                            food_id
                        )
                        color_print(
                            "normal",
                            "Le produit à été supprimé des favoris"
                        )
                        loop = True
                    else:
                        functions.not_in_list()

                else:
                    functions.not_int()
