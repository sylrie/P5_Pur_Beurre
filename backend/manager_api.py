""" managerAPI
    manage the API request
"""

#! /usr/bin/env python3
# coding: UTF-8

from requests import get

class ManagerApi():
    """ manage the API request """

    def __init__(self):

        self.categories = (
            "Saucisson",
            "Pizza",
            "Chips",
            "Yaourts",
            "Biscuits"
            )

        self.food_list = []

        self.add_data()

    def request_api(self, category_name):
        """ Make a API request for a selected category"""

        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": "{}".format(category_name),
            "page_size": "25",
            "json": "1",
            "page": "1"
            }

        request = get(url=url, params=params)

        return request.json()

    def add_data(self):
        """ Add foods into food_list"""

        for category in self.categories:

            data = self.request_api(category_name=category)

            for product in data["products"]:

                food_data = {
                    "Category": "",
                    "Food_Name": "",
                    "Generic_Name": "",
                    "Brand": "",
                    "Nutrigrade": "",
                    "Link": "",
                    "Stores": "",
                    }

                try:

                    food_data["Category"] = category
                    food_data["Food_Name"] = product["product_name"]
                    food_data["Generic_Name"] = product["generic_name"]
                    food_data["Brand"] = product["brands"]
                    food_data["Nutrigrade"] = product["nutrition_grades"]
                    food_data["Link"] = product["url"]
                    food_data["Stores"] = product["stores"]

                    self.food_list.append(food_data)

                except Exception as err:
                    print(err)
