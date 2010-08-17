from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Ristorante, Piatto

def index(request):
    ristoranti = Ristorante.objects.all()
    return render_to_response('index.html', RequestContext(request, {'ristoranti': ristoranti}))

def show(request, restourant_id):
    r = Ristorante.objects.get(id = restourant_id)
    return render_to_response('show.html', RequestContext(request,{'r': r}))

def piatti(request):
    plates = Piatto.objects.all()
    return render_to_response('piatti.html', RequestContext(request, {'piatti': plates}))