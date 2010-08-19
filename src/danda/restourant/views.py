from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Ristorante, Piatto, Ordine
from django.contrib.auth.decorators import login_required

def index(request):
    ristoranti = Ristorante.objects.all()
    return render_to_response('index.html', RequestContext(request, {'ristoranti': ristoranti}))

def about(request):
    return render_to_response('about.html', RequestContext(request))

def show(request):
    ristoranti = Ristorante.objects.all()
    return render_to_response('index.html', RequestContext(request, {'ristoranti': ristoranti}))

def show_restourant(request, restourant_id):
    r = Ristorante.objects.get(id = restourant_id)
    return render_to_response('show.html', RequestContext(request,{'r': r}))

def piatti(request):
    ristoranti = Ristorante.objects.all()
    plates = Piatto.objects.all()
    return render_to_response('piatti.html', RequestContext(request, {'piatti': plates}))

@login_required
def ordini(request):
    ordini = Ordine.objects.filter(user = request.user)
    return render_to_response('ordini.html', RequestContext(request, {'ordini': ordini}))

@login_required
def show_ordine(request, id_ordine):
    ordine = Ordine.objects.get(id = id_ordine)
    return render_to_response('show_ordine.html', RequestContext(request, {'ordine': ordine}))