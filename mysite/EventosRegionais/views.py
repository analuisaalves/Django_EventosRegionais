from django.shortcuts import render

from . import models

#create your views here.
def pagina_principal(requerest):
    eventos = models.Evento.objects.all()
    return render(requerest, "index.html",{
        "eventos": eventos,
        "titulo": "Meus Eventos"})
