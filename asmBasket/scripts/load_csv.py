import csv
from players.models import Joueur

def run():
    file = open('new_data.csv')
    reader = csv.reader(file)

    Joueur.objects.all().delete()

    for row in reader:
        print(row)

        player, is_created = Joueur.objects.get_or_create(nom=row[1], prenom=row[2], adresse=row[3], code_postal=row[4], 
            intra_extra=row[5], age=row[6], naissance=row[7], licence=row[8], genre=row[9], taille=row[10], prix=row[11], categorie=row[12])


