from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Ristorante, Piatto, Ordine, Portata, Elemento
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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
    portate = Portata.objects.all()
    print ristoranti[0].nome
    return render_to_response('piatti.html', RequestContext(request, {'portate': portate, 'ristoranti': ristoranti}))

@login_required
def ordini(request):
    ordini = Ordine.objects.filter(user = request.user)
    return render_to_response('ordini.html', RequestContext(request, {'ordini': ordini}))

@login_required
def show_ordine(request, id_ordine):
    ordine = Ordine.objects.get(id = id_ordine)
    return render_to_response('show_ordine.html', RequestContext(request, {'ordine': ordine}))

@login_required
def nuovo_ordine(request):
    from forms import OrdineForm
    if request.method == 'POST':
        f = OrdineForm(request.POST)
        if f.is_valid():
            print "CCCA"
            print f.cleaned_data
            r = Ristorante.objects.get(id = int(f.cleaned_data.pop('restourant')))
            a = Ordine(user = request.user, ristorante = r)
            a.save()
            for k in f.cleaned_data:
                p = Portata.objects.get(id = int(k))
                e = Elemento(piatto = Piatto.objects.get(portata = p, ristorante = r), numero = f.cleaned_data[k])
                e.save()
                a.elementi.add(e)
    else:
        f = OrdineForm()
    return render_to_response('nuovo_ordine.html', RequestContext(request, {'f': f}))

