""" managerDB
    Manage the Database
"""

#! /usr/bin/env python3
# coding: UTF-8

# library import
from getpass import getpass
import json
import mysql.connector

# programs import
import backend.functions as function
from backend.manager_api import ManagerApi


class ManagerDb():
    """ Manage the Database """

    def __init__(self):

        self.connection = self.check_database()

        self.init_food()

    def check_database(self):
        """ check if database exists """

        with open("backend/options.json") as options:
            data = json.load(options)

        if data[0]["initialised"] == "true":
            connection = self.get_connection()

        else:
            connection = self.first_connection()

        return connection

    def first_connection(self):
        """ Collect intels for conection """

        check = False
        with open("backend/options.json") as options:
            data = json.load(options)
            function.color_print(
                "normal",
                "Connection à Mysql:"
            )

            while not check:
                function.color_print(
                    "normal",
                    "Nom utilisteur:"
                )
                user = input()

                function.color_print(
                    "normal",
                    "Le mot de passse ne s'affichera pas"
                )
                function.color_print(
                    "normal",
                    "Mot de passe:"
                )
                password = getpass("")

                function.color_print(
                    "normal",
                    "Hote:"
                )
                host = input()

                coded_password = function.coding(password, "code")

                data[0]["user"] = user
                data[0]["password"] = coded_password
                data[0]["host"] = host

                with open("backend/options.json", "w") as options:
                    json.dump(data, options)

                try:
                    connection = mysql.connector.connect(
                        user=user,
                        password=password,
                        host=host,
                    )

                    check = True
                    return connection

                except Exception as e:
                    print(e)
                    function.color_print(
                        "error",
                        "---Erreur de connection, Veuillez recommencer---"
                    )

    def get_connection(self):
        """ connection to Mysql database """

        with open("backend/options.json") as options:
            data = json.load(options)

            password = function.coding(data[0]["password"])

        try:
            connection = mysql.connector.connect(
                user=data[0]["user"],
                password=password,
                host=data[0]["host"],
                database=data[0]["database"]
            )

            return connection

        except Exception as e:
            print(e)

    def query(self, sql, val=None):
        """ make query for database """

        cursor = self.connection.cursor()

        if val is not None:
            try:
                cursor.execute(sql, val)

            except Exception as e:
                print(e)

            cursor.close()
            self.connection.commit()

        else:
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()

                return result

            except Exception as e:
                print(e)

        cursor.close()
        self.connection.commit()

    def create_tables(self):
        """ Create tables for database """

        with open("backend/script.sql", "r") as tables:
            database = tables.read()

        cursor = self.connection.cursor()
        sql_commands = cursor.execute(database, multi=True)

        try:
            # Reading command line
            for command_line in sql_commands:
                pass

        except Exception:
            print(e)

    def init_food(self):
        """ Add datas in food table """

        with open("backend/options.json") as options:
            data = json.load(options)
        if data[0]["initialised"] == "false":

            function.color_print(
                "normal",
                "Création de la Base de Données..."
            )
            self.create_tables()

            function.color_print(
                "normal",
                "Importation des données d'Open Food Facts..."
            )

            food_list = ManagerApi().food_list
            #cursor = self.connection.cursor()

            for food in food_list:

                sql = """INSERT INTO Food (
                        Category,
                        Food_Name,
                        Brand, Stores,
                        Link,
                        Nutrigrade
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )"""

                val = (
                    food.get("Category"),
                    food.get("Food_Name"),
                    food.get("Brand"),
                    food.get("Stores"),
                    food.get("Link"),
                    food.get("Nutrigrade")
                )

                self.query(sql, val)

            data[0]["initialised"] = "true"

            with open("backend/options.json", "w") as options:
                json.dump(data, options)

            function.color_print(
                "normal",
                "Les données d'Open Food Facts ont été ajoutées"
            )

        else:
            pass
