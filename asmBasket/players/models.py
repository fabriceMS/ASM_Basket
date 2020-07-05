from django.db import models

# Create your models here.
class Saison(models.Model):
    nom = models.CharField(max_length=100)
    Date = models.DateTimeField()

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    categorie = models.CharField(max_length=100)
    tarif_intra = models.IntegerField()
    tarif_extra = models.IntegerField()

    def __str__(self):
        return self.categorie


class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    commune = models.CharField(max_length=100)
    intra_extra = models.CharField(max_length=10)
    categorie = models.CharField(max_length=100)
    prix = models.IntegerField()
    #categorie = models.ForeignKey()
    #saison = models.ForeignKey()
    age = models.IntegerField()
    naissance = models.DateTimeField()
    licence = models.IntegerField()
    genre = models.CharField(max_length=1)
    taille = models.IntegerField()



    def __str__(self):
        return '{} {}'.format(self.nom, self.prenom)
