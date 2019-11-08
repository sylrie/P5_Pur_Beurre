#! /usr/bin/env python3
# coding: UTF-8

# library import
import string


def color_print(code, message):
    """ Display message with selected color"""

    if code == "error":
        color = "3;31;40m"

    elif code == "normal":
        color = "1;32;40m"

    elif code == "data":
        color = "6;33;40m"

    elif code == "link":
        color = "3;34;40m"

    print('\x1b[{}'.format(color) + message + '\x1b[0m')

def cesar(chain, dec):
    """ Use Cesar method for coding characters"""

    alph = string.ascii_uppercase
    character = chain.upper()
    return character.translate(str.maketrans(alph,alph[dec:]+alph[:dec]))

def coding(password, action=None):
    """ select the key for Cesar method and check characters"""
    
    # key for code or uncode
    if action == "code":
        key = 10
    else:
        key = -10

    to_crypt =[]

    for character in password:
        
        if character.lower() == character:
            new_character = cesar(character.upper(), key)
            coded = new_character.lower()
        else:
            coded = cesar(character, key)
        
        to_crypt.append(coded)
    
    mdp = "".join(to_crypt)

    return(mdp)

def check_input(to_check):
    """ Check if input is integer """

    try:
        to_check = int(to_check)
        return True
    
    except ValueError:
        return False

def not_int():
    """ Print error not integer """

    color_print(
        "error",
        "---Veuillez entrer un chiffre---"
    )

def not_in_list():
    """ Print error not in list """

    color_print(
        "error",
        "---Oups! le choix n'est pas dans la liste---"
    )