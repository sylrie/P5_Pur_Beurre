#! /usr/bin/env python3
# coding: UTF-8

from getpass import getpass
import mysql.connector
import json

import methods
from managerAPI import ManagerAPI


class ManagerDB():

    def __init__(self):
        
        
        self.connection = self.check_database()
        self.init_food()
        
    def check_database(self):

        with open("options.json") as options:
            data = json.load(options)

        if data[0]["initialised"] == "true":
            connection = self.get_connection()
        
        else:
            connection = self.first_connection()
            
        return(connection)

    def first_connection(self):
        check = False
        with open("options.json") as options:
            data = json.load(options)
            methods.color_print("normal", "Connection à Mysql:")
            while not check:
                methods.color_print("normal", "Nom utilisteur:")
                user = input()

                methods.color_print("normal", "Le mot de passse ne s'affichera pas")
                methods.color_print("normal", "Mot de passe:")
                password = getpass("")

                methods.color_print("normal", "Hote:")
                host = input()

                coded_password = methods.coding(password, "code")

                data[0]["user"] = user
                data[0]["password"] = coded_password
                data[0]["host"] = host

                with open("options.json", "w") as options:
                    json.dump(data, options)

                try:
                    connection = mysql.connector.connect(
                        user=user,
                        password=password,
                        host=host,
                    )
                    check
                    return(connection)

                except Exception as e:
                    methods.color_print("error", "---Erreur de connection, Veuillez recommencer---")
                
    def get_connection(self):

        with open("options.json") as options:
            data = json.load(options)

            password = methods.coding(data[0]["password"])

        try:
            connection = mysql.connector.connect(
                user=data[0]["user"],
                password=password,
                host=data[0]["host"],
                database=data[0]["database"]
            )
            return(connection)

        except Exception as e:
            pass

    def query(self, sql, val=None):

        cursor = self.connection.cursor()

        if val != None:
            try:
                cursor.execute(sql, val)
            
            except Exception as e:
                pass

            cursor.close()
            self.connection.commit()

        else:    
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()
                return(result)

            except Exception as e:
               pass
            
        cursor.close()
        self.connection.commit()

    def query_favorites(self, sql, userid):
        
        cursor = self.connection.cursor()

        try:
            cursor.execute(sql)
            
        except Exception as e:
            pass
            
        result = cursor.fetchall() 
        
        cursor.close()
        return(result)

    def create_tables(self):

        with open("script.sql","r") as tables:
            database = tables.read()

        cursor = self.connection.cursor()
        sql_commands = cursor.execute(database, multi=True)
    
        try:
            # Reading command line
            for command_line in sql_commands:
                pass
                
        except Exception as e:
            print(e)

    def init_food(self):

        with open("options.json") as options:
            data = json.load(options)
        if data[0]["initialised"] == "false":

            methods.color_print("normal", "Création de la Base de Données...")
            self.create_tables()

            methods.color_print("normal", "Importation des données d'Open Food Facts...")

            food_list = ManagerAPI().food_list
            cursor = self.connection.cursor()

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

            with open("options.json", "w") as options:
                json.dump(data, options)
            
            methods.color_print("normal", "Les données d'Open Food Facts ont été ajoutées")
        
        else:
            pass
