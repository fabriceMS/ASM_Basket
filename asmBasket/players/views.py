from django.shortcuts import render
from .models import Joueur

# Create your views here.
def home(request):
    
    players = Joueur.objects.all()

    nb_intra = Joueur.objects.filter(intra_extra='INTRA').count()
    nb_extra = Joueur.objects.filter(intra_extra='INTRA').count()

    prix_pour_intra = nb_intra * 5
    prix_pour_extra = nb_extra * 10
    total = prix_pour_intra + prix_pour_extra




    context = {
        'players': players,
        'nb_intra': nb_intra,
        'nb_extra': nb_extra,
        'prix_intra': prix_pour_intra,
        'prix_extra': prix_pour_extra,
        'total_retour': total,
    }

    return render(request, 'players/index.html', context)