from django.shortcuts import render
from .models import Carmake, Model


def index(request):
    carmakes = Carmake.objects.all()
    return render(request, 'index.html', {'carmakes': carmakes})

def get_models(request, carmake_id):
    carmake = Carmake.objects.get(pk=carmake_id)
    models = Model.objects.filter(carmake=carmake)
    return render(request, 'models.html', {'models': models})
