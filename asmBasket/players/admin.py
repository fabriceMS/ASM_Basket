from django.contrib import admin
from players.models import Saison, Categorie, Joueur


@admin.register(Saison)
class SaisonAdmin(admin.ModelAdmin):
    search_fields = ['nom']


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ['categorie']

    list_display = (
        'categorie',
        'age_min',
        'age_max',
        'tarif_intra',
        'tarif_extra',
    )

    ordering = ('age_min',)


@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    search_fields = ['nom']


    list_display = (
        'nom',
        'prenom',
        'naissance',
        'age',

    )