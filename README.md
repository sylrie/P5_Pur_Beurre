<p align="center">
    <img width=50% src="https://github.com/sylrie/P5_Pur_Beurre/blob/master/img/P5.png">
</p>
<p align="center">
    <img width=30% src="https://github.com/sylrie/P5_Pur_Beurre/blob/master/img/openfoodfacts.png">
</p>

> PROJET 5 OpenClassrooms - Substiute product - Pur Beurre

The goal of *Pur Beurre* is to create a program that interacts with the Open Food Facts database for compare food and propose a healthier substitute for the food.

## REQUIREMENTS

* Python 3 
* MySQL Database and a connexion to MySql serveur

- Install Python 3.8 https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
- Install Mysql: https://dev.mysql.com/downloads/


## START

* 1.**Clone** or **download** the repository:
<P> https://github.com/sylrie/P5_Pur_Beurre.git</p>

* 2.Install **packages**:
<p> Select on the Shell the repository:</p>
exemple:
```shell
C:\Users\Users\Admin\Desktop\P5_Pur_Beurre>
```

then launch this commande line:
```
pip install -r requirements.txt
```

* 3.Launch the program:
```
python main.py
```

* 4.Your **MySQL informations** will be required for the first use.


## DESCRIPTION

On terminal, the user receive multiple choice:
* 1-What food do you want to replace ?
* 2-Find my substituted fodds.

If the user **return 1**,
- the application offers the following questions to the user:

* 1.Select the category. [Several propositions associated with a number. The user return the number corresponding and press enter]
* 2.Select the food. [Several propositions associated with a number. The user return the number corresponding to the chosen food and press enter]

* The application offers a substitute, its description, a store where buy it and a link to the page Open Food Facts about this food
* The user has the possibility to save the result in the database.

If the user **return 2**,
- the application offers the results saved in database.


## FEATURES

* Search for food in the **Open Food Facts API**.
* The application offers a substitute, its description, a store where buy it and a link to the page Open Food Facts.
* Interaction of the user with the program in the terminal.
* Management of user input errors.
* Using a **MySql database**.