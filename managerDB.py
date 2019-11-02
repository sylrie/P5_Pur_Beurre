#! /usr/bin/env python3
# coding: UTF-8

from getpass import getpass
import mysql.connector
import json
import pprint

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

        with open("options.json") as options:
            data = json.load(options)
            print("connection à Mysql:")
            user = input("Nom utilisteur: ")
            password = getpass("Mot de passe: ")
            #password = input("Password: ")
            host = input("host: ")

            data[0]["user"] = user
            data[0]["password"] = password
            data[0]["host"] = host

            with open("options.json", "w") as options:
                json.dump(data, options)

            try:
                connection = mysql.connector.connect(
                    user=user,
                    password=password,
                    host=host,
                )
                return(connection)

            except Exception as e:
                pass
                
    def get_connection(self):

        with open("options.json") as options:
            data = json.load(options)

        try:
            connection = mysql.connector.connect(
                user=data[0]["user"],
                password=data[0]["password"],
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
                #for row in result:
                    #print(row)

            except Exception as e:
               pass
            
        #cursor.close()
        #self.connection.commit()

    def query_favorites(self, sql, userid):
        cursor = self.connection.cursor()

        try:
                cursor.execute(sql)
            
        except Exception as e:
            pass
            
        result = cursor.fetchall() 
        for row in result:
            if row[0] == userid:
                print(row[1])
            else:
                pass

        cursor.close()

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

            print("Création de la Base de Données...")
            self.create_tables()

            print("importation des données d'Open Food Facts...")

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
            print("Les données d'Open Food Facts ont été ajoutées")
        
        else:
            pass
