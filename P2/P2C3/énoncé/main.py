def salaire_mensuel(salaire_annuel):
    return salaire_annuel/12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel/4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire/ heures_travaillees

#Demandez à l'utilisateur de saisir son salaire annuel.

salaire_annuel= float(input("donne moi ton saliare:"))
heures_travaillees = float(input("donne ton heure hebdomadaire par semaine:"))
mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)
print(f"Mon salaire est, {horaire}")
