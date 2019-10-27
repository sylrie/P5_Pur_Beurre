#! /usr/bin/env python3
# coding: UTF-8

import mysql.connector
import json
import pprint

from managerAPI import ManagerAPI


class ManagerDB():

    def __init__(self):

        self.password = "CDBloule30"
        self.user = "root"
        self.host = "localhost"
        self.database = "P5_Pur_Beurre"

        self.connection = self.get_connection()

    def get_connection(self):

        try:
            connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
            
            return connection

        except Exception as e:
            pass

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
            pass

    def add_food(self):

        with open("options.json") as options:
            data = json.load(options)

        if data[0]["Initialised"] == "false":
            
            self.create_tables()
            food_list = ManagerAPI().food_list

            for food in food_list:
                
                cursor = self.connection.cursor()
                try:
                    cursor.execute("""
                        INSERT INTO Food (
                            Category, Food_Name, Brand, Stores, Link, Nutrigrade
                        )
                        VALUES (
                            %s, %s, %s, %s, %s, %s
                        )""",(
                            food.get("Category"),
                            food.get("Food_Name"),
                            food.get("Brand"),
                            food.get("Stores"),
                            food.get("Link"),
                            food.get("Nutrigrade")
                            )
                    )
                    cursor.close()
                    

                except Exception as e:
                    pass

            self.connection.commit()

            data[0]["Initialised"] = "true"

            with open("options.json", "w") as options:
                json.dump(data, options)

            '''cursor = self.connection.cursor()
            cursor.execute("""
            SELECT * FROM Food""")

            for row in cursor:
                pprint.pprint(row)
            cursor.close()'''

t = ManagerDB()
test = t.add_food()