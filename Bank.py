# Science de l'ingénieur

import random
from math import floor

Employees = []
id_Employ = []


def calculer_salaire(age):
    if age > 50:
        return 12000
    else:
        if 18 < age < 30:
            return 5000
        if 30 <= age < 45:
            return 7500
        if 45 <= age < 50:
            return 10000


def anciennete(years):
    if 0 <= years <= 3:
        return 0
    if 4 <= years <= 6:
        return 1000
    if 7 <= years <= 10:
        return 2000
    if 11 < years:
        return 3000 + random.randint(0, 8000)  # pour les primes


def number_of_kids(kids):
    if kids == 0:
        return 0
    if kids == 1:
        return 700
    if kids == 2:
        return 1500
    if kids == 3:
        return 2000
    if kids >= 4:
        return floor((kids + 1000)/kids)


def afficher_liste_employes():
    print("\nListe des employés :")
    for i, employee in enumerate(Employees, start=1):
        print(f"{i}. Nom: {employee['name']}, ID: {employee['employee_id']}, Salaire: {employee['salary']} DH")


def principal():
    age = int(input("Entrez l'âge de l'employé :                                      "))
    years = int(input("Depuis combien d'années cette parsonne travail dans la société : "))
    num = int(input("Nombre d'enfants :                                               "))

    salaire = calculer_salaire(age) + number_of_kids(num) + anciennete(years)

    if age - years <= 18:
        print("Illegal")
    else:
        employee_data = {'name': input("Entrez le nom de l'employé :                                     "),
                         'employee_id': input("Entrez l'ID de l'employé :                                       "),
                         'salary': salaire}
        Employees.append(employee_data)
        afficher_liste_employes()


isTrue = True

while True:
    principal()
    if int == "Continue":
        principal()
    if int == "QUIT" or int == "quitter" or int == "fermer" or int == "stop":
        isTrue = False


