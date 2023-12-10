def calculer_salaire(age):
    if age > 50:
        return 6000
    else:
        return 3000

def principal():
    try:
        age = int(input("Entrez l'âge de l'employé : "))

        salaire = calculer_salaire(age)

        print(f"Le salaire de l'employé est : {salaire} euros")
    except ValueError:
        print("Saisie invalide. Veuillez entrer un âge valide en tant que nombre.")


if __name__ == "main":
    principal()
