""" tableDB
    Manage tables of database
"""

#! /usr/bin/env python3
# coding: UTF-8

# programs import
from backend.manager_db import ManagerDb


def add_user(user_name, user_password=None):
    """ add a user in users table"""

    sql = """INSERT INTO users (
            username,
            userpassword
        )
        VALUES (
            %s,
            %s
    )"""

    val = (
        user_name,
        user_password
    )

    query = ManagerDb().query(sql, val)

def show_table(table):
    """ look values on selected table"""

    sql = """SELECT * FROM {}""".format(table)

    query = ManagerDb().query(sql)

    return query

def show_value(value, table, column, column_value):
    """ look values for selected table and selected value """

    sql = """SELECT {}
        FROM {}
        WHERE {}
        ='{}'
        LIMIT 5
        """.format(
            value,
            table,
            column,
            column_value
        )

    query = ManagerDb().query(sql)

    return query

def show_mutli( value, table, columns, column_values):
    """ look values for selected table and selected values """

    sql = """SELECT {}
        FROM {}
        WHERE {}
        ='{}'
        AND {}
        ='{}'
        LIMIT 2""".format(
            value,
            table,
            columns[0],
            column_values[0],
            columns[1],
            column_values[1]
        )

    query = ManagerDb().query(sql)

    return query

def add_favorite(user_id, food_id):
    """ Add a favorite in Favorites table """

    duplicate = show_value("foodid", "favorites", "foodid", food_id)

    if not duplicate:

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

        query = ManagerDb().query(sql, val)
        message = "Le produit à été ajouté à vos favoris"

    else:
        message = "Ce produit est déja dans les favoris"

    return message

def action_values(action, table, column, value):
    """ make selcted action on selected table """

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

    query = ManagerDb().query(sql)