def addition(nombreA, nombreB):
    return nombreA + nombreB

def multiplication(nombreA, nombreB):
    return nombreA * nombreB

def soustraction(nombreA, nombreB):
    return nombreA - nombreB

def division(nombreA, nombreB):
    if nombreB == 0:
        raise ValueError("Impossible de diviser par 0.")
    return nombreA / nombreB

# Demande un choix
choix = None
while choix not in {1, 2, 3, 4}:
    choix = int(input("Que souhaitez-vous faire ?\n\n 1 - Addition\n 2 - Multiplication\n 3 - Soustraction\n 4 - Division\n"))

premier_nombre = None
deuxieme_nombre = None
while not isinstance(premier_nombre, (int, float)) or not isinstance(deuxieme_nombre, (int, float)):
    try:
        premier_nombre = float(input("Entrez un premier nombre :"))
        deuxieme_nombre = float(input("Entrez un deuxième nombre : "))
    except ValueError:
        print("Veuillez saisir des nombres valides.")

try:
    if choix == 1:
        resultat = addition(premier_nombre, deuxieme_nombre)
    elif choix == 2:
        resultat = multiplication(premier_nombre, deuxieme_nombre)
    elif choix == 3:
        resultat = soustraction(premier_nombre, deuxieme_nombre)
    elif choix == 4:
        resultat = division(premier_nombre, deuxieme_nombre)
    else:
        raise ValueError("Une erreur est survenue.")

    print("Voici le résultat :", resultat)
except ValueError as error:
    print(error)  
