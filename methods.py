import string


def color_print(code, message):

        if code == "error":
            color = "3;31;40m" 
        elif code == "normal":
            color = "1;32;40m"
        elif code == "data":
            color = "6;33;40m"
        elif code == "link":
            color = "3;34;40m"
        
        print('\x1b[{}'.format(color) + message + '\x1b[0m')

def cesar(chaine,dec) :
    alph = string.ascii_uppercase
    character = chaine.upper()
    return character.translate(str.maketrans(alph,alph[dec:]+alph[:dec]))

def coding(password, action=None):
    
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
