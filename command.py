import pprint

category = {"1": "Saucisson","2": "Pizza"}
selected_category = ""
value = ""

while value != "q":
    
    print("Liste des catégories")
    pprint.pprint(category)
    value = input("Choisissez un numéro de catégorie ")

    if value not in category:
        print("Sorry! we can't find the selected category, please try again :)")
    else:
        selected_category = category[value]
        

    print("{} food list".format(selected_category))
    print("la liste d'aliment, faire un choix")
    value = input("chose a food number: ")