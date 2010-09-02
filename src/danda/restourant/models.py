# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Ristorante(models.Model):
    nome = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 15)
    indirizzo = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = 'Ristoranti'
    def __unicode__(self):
        return self.nome

class Portata(models.Model):
    name = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = 'Portate'
    def __unicode__(self):
        return self.name

class Piatto(models.Model):
    portata = models.ForeignKey(Portata)
    ristorante = models.ForeignKey(Ristorante)
    prezzo = models.FloatField()
    class Meta:
        verbose_name_plural = 'Piatti'
    def __unicode__(self):
        return "%s (%s) Euro: %2.2f" % (self.portata, self.ristorante, self.prezzo)

class Elemento(models.Model):
    piatto = models.ForeignKey(Piatto)
    numero = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Elementi'
    def __unicode__(self):
        return "%2d - %s" % (self.numero, self.piatto)

    def totale(self):
        return self.numero * self.piatto.prezzo

    def totale_altro(self, ristorante):
        altro_piatto = Piatto.objects.get(portata = self.piatto.portata, ristorante = ristorante)
        return self.numero * altro_piatto.prezzo

class Ordine(models.Model):
    user = models.ForeignKey(User)
    elementi = models.ManyToManyField(Elemento)
    ristorante = models.ForeignKey(Ristorante)
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'Ordini'

    def totale(self):
        return sum([e.totale() for e in self.elementi.all()])

    def totale_altro(self, ristorante):
        return sum([e.totale_altro(ristorante) for e in self.elementi.all()])

    def altri_ristoranti(self):
        rists = Ristorante.objects.exclude(id = self.ristorante.id)
        return ["%s = %.2f" % (i.nome, self.totale_altro(i)) for i in rists]
