
#! /usr/bin/env python3
# coding: UTF-8

import mysql.connector
import json
from random import randrange

from methods import color_print
from managerDB import ManagerDB
from managerAPI import ManagerAPI
from tablesDB import Tables



class Program():

    def __init__(self):

        self.check_database = ManagerDB()
        self.categories = ManagerAPI().categories
        self.loop = True
        self.selected_category = ""
        self.user = ""
        
        self.program_loop()

    def select_user(self):
        
        users = Tables().show_table("users")
        
        color_print("data", "Liste utilisateur(s) :")

        count = 0
        
        for row in users:
            count += 1
            color_print("data", "{} : {}".format(row[0],row[1]))

        if count == 0:
            color_print("error", "La liste est vide :(")
            color_print("normal", "Vous devez créer un utilisateur")
            self.new_user()
            
        else:
            check = False
            while check == False:
                
                color_print("normal", "Veuillez entrer le NUMERO d'utilisateur ('+' pour nouveau)")
                nbr = input()

                if nbr == "+":
                    check = True
                    self.new_user()
                
                else:
                    try:
                        if int(nbr) - 1 in range(len(users)):
                            check = True
                            username = Tables().show_value('UserName','Users', 'id', nbr)
                            color_print("normal", "Bienvenue {} !".format(username[0][0]))
                            self.user = nbr

                        else:
                            color_print("error", "---Le numéro n'est pas dans la liste!---")
                    except:
                        color_print("error", "---Veuillez entrer un chiffre!---")
    
    def new_user(self):

        color_print("normal", "Veuillez entrez votre nom:")
        username = input()
        color_print("normal", "Veuillez entrer un pseudo:")
        userpseudo = input()

        Tables().add_user(username,userpseudo)
        color_print("normal", "L'utilisateur {}, {} à été crée.".format(username, userpseudo))

        self.select_user()
    
    def program_loop(self):
        
        color_print("normal", "Bonjour!")
        while self.loop:

            action = self.action_choice()
            if action == "1":
                self.select_category()
                self.select_food()
            elif action == "2":
                print("favorites")
        color_print("normal", "A bientôt !")  

    def action_choice(self):
        
        check = False
        while check == False:

            color_print("data", "1 - Quel aliment souhaitez-vous remplacer ?")
            color_print("data", "2 - Retrouver mes aliments substitués.")

            color_print("normal", "Entrez le NUMERO correspondant à votre choix: ('q' pour quitter)") 
            action = input()

            if action == "1" or action == "2":
                check = True
                return(action)

            elif action == "q":
                check = True
                self.loop = False

            else:
                color_print("error", "---Oups! le choix doit être 1 ou 2---")

    def select_category(self):
        
        check = False
        while check == False:

            color_print("data", "Affichage des catégories...")
            
            cat = 0
            for category in self.categories:
                cat += 1
                color_print("data", "{} : {}".format(cat, category))
            
            color_print("normal", "Veuillez entrez le NUMERO de la catégorie: ")
            cat = input()

            try:
                cat = int(cat) - 1
                
                if cat in range(len(self.categories)):
                    check = True
                    self.selected_category = self.categories[cat]
                else:
                    color_print("error", "---Le numéro n'est pas dans la liste!---")
            
            except:
                color_print("error", "---Veuillez entrer un chiffre!---")

    def select_food(self):

        color_print("normal", "Produits de la catégorie {}:".format(self.selected_category))
        result = Tables().show_value("id, Food_name, Brand", "Food", "Category", self.selected_category)

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
        check = False
        while check == False:

            color_print("normal", "Choissez un NUMERO d'aliment :")
            select = input()
            
            try:
                
                if int(select) - 1 in range(len(result)):

                    id_selected = result[int(select)-1][0]
                    
                    color_print("data", "Vouz aves selectionné le produit:")
                    color_print("normal", result[int(select)-1][1])
                    check = True
                    
                else:
                    color_print("error", "---Le numéro n'est pas dans la liste!---")
            except:
                color_print("error", "---Veuillez entrer un chiffre!---")

        self.substitute(id_selected)

    def substitute(self, id_selected):
            
        nutriscores = ["a", "b", "c", "d", "e"]

        result = Tables().show_value("*", "Food", "id", id_selected)

        nutrigrade = result[0][7]
        color_print("normal", "Ce produit à pour nutrigrade: {} ".format(nutrigrade))
        
            
        for score in nutriscores:
            substitute_nutriscore = score
            food = Tables().show_mutli("*", "Food", "category", self.selected_category, "Nutrigrade", score)
            
            if nutrigrade == substitute_nutriscore:
                color_print("error", "Nous n'avons pas de prodruit avec un meilleur nutriscore à proposer")
            if len(food) > 0:
                break
        
        color_print(
            "normal", 
            "Nous vous proposons ces poduits avec un nutrigrade de: {} "
                .format(
                substitute_nutriscore
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
            color_print("link", "(liens: {})".format(product[6]))
            
            count += 1

        check = False
        while check == False:
            color_print("normal", "Souhaitez vous enregistrer un de ces subsituts dans vos favoris? (o/n)")
            action = input()

            if action == "o":
                print("attend c'est pas pret")
                check = True

            elif action == "n":
                check = True            
            
            else:
                color_print("error", "---La réponse doit être 'o' pour oui ou 'n' pour non---")
            
t = Program()
#test = t.select_category()