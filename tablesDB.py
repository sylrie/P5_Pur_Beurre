import mysql.connector
import json
from managerDB import ManagerDB

class Tables():

    def __init__(self):

        self.user_id = 1

    """def drop_table(self, table):

        sql = "DROP TABLE {}".format(table)
        query = ManagerDB().query(sql)

        if table == "food":
            self.drop_table('Favorites')
            query = ManagerDB().query(sql)
            with open("options.json") as options:
                data = json.load(options)

            data[0]["Initialised"] = "false"

            with open("options.json", "w") as options:
                json.dump(data, options)"""

    def add_user(self,username, userpseudo):
        
        sql = """INSERT INTO Users (
                UserName,
                Userpseudo
            )
            VALUES (
                %s,
                %s
        )"""

        val = (
            username,
            userpseudo
        )
        
        query = ManagerDB().query(sql,val)
    
    def show_table(self, table):

        sql = """SELECT * FROM {}""".format(table)
        
        query = ManagerDB().query(sql)
        
        return(query)

    def show_value(self, value, table, column,column_value):

        sql = """SELECT {}
            FROM {}
            WHERE {}
            ='{}'
            """.format(
                value,
                table,
                column,
                column_value
            )

        query = ManagerDB().query(sql)
        
        return(query)

    def show_mutli(self, value, table, column, column_value, column2, column_value2):

        sql = """SELECT {}
            FROM {}
            WHERE {}
            ='{}'
            AND {}
            ='{}'
            """.format(
                value,
                table,
                column,
                column_value,
                column2,
                column_value2
            )

        query = ManagerDB().query(sql)
        
        return(query)
        
    def delete_value(self):

        sql = """DELETE FROM {} W"""
    
    def add_favorite(self, user_id, food_id):

        sql = """INSERT INTO Favorites (
            UserID,
            FoodID
            )
            VALUES (
                %s,
                %s
        )"""

        val = (
            user_id,
            food_id
        )

        query = ManagerDB().query(sql,val)
        
    def action_values(self,action, table, column, value):

        sql = """{} 
            FROM {} 
            WHERE {}
            ='{}'
            """.format(
                action,
                table,
                column,
                value
            )

        query = ManagerDB().query(sql)
    
    def show_favorites(self):

        sql = "SELECT \
                favorites.UserID AS user, \
                food.food_name AS favorite \
                FROM Favorites\
                INNER JOIN food ON favorites.FoodID = Food.ID"
        
        query = ManagerDB().query_favorites(sql, self.user_id)
