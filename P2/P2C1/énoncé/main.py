nombre1 = input("donne un 1er nombre")
nombre2 = input("donne un 2er nombre")
if nombre1.isnumeric() and nombre2.isnumeric():
    print("ce sont des nombre numerique") ## isnumeric() permet de vérifier si la chaîne de caractères est un nombre
    raise SystemExit("Fin du programme")
else:
    print(nombre1 = int(nombre1) and nombre2 == int(nombre2))


 operateur= input("donne un operateur")
if (operateur in ["+", "-", "*", "/"]):
    print("l'operarateur", operateur, "est valide")
else:
    print("Fin du programme")
    raise SystemExit("Fin du programme")

  
    nombre1 = int(input("donnez un 1er nombre"))
nombre2 = int(input("donnez un 2eme nombre"))
operateur = input("saisissez un operateur")
resultat = nombre1 operateur nombre2
if operateur not in ["+", "-", "*", "/" ]:
    print("Erreur: l'operateur doit appatenir à '+', '-', '*', '/'")
elif operateur == "+" :
    resultat = nombre1 + nombre2
elif operateur == "-":
    resultat = nombre1 - nombre2
elif operateur == "*":
    resultat = nombre1 * nombre2
elif operateur =="/":
        if nombre2 != 0:
            resultat = round(nombre1 / nombre2, 2)
        else:
            print("erreur: impossible de diviser un nombre par 0")
            raise systemExit("Fin du programme")

print(f"le resultat de l'operateur est:{round(resultat,2)}")
   
