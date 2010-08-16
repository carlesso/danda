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
        
class Ordine(models.Model):
    user = models.ForeignKey(User)
    elementi = models.ManyToManyField(Elemento)
    class Meta:
        verbose_name_plural = 'Ordini'
