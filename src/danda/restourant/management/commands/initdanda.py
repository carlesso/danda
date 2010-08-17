# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from danda.restourant.models import Ristorante, Portata, Piatto
from random import randint

piatti = [('Involtini Primavera', 1.00),
          ('Gnocchi Fritti', 2.50),
          ('Gamberi al Vapore', 3.50),
          ('Spaghetti di Soia', 3.00),
          ('Spaghetti di Mare', 4.00),
          ('Pollo in Agrodolce', 3.50),
          ('Pollo alle Mandorle', 3.00),
          ('Pollo al Limone', 2.50),
          ('Ravioli al vapore', 2.80),
          ('Riso Cantonese', 2.50),
          ('Spachetti di Soia alla Piastra', 3.00),
          ]


class Command(BaseCommand):
    args = "None"
    help = "Inizializza il progetto danda con dei dati di esempio"
    def handle(self, *args, **kargs):
        print "Creating admin user"
        a = User.objects.create_superuser('admin', 'marcopaster@libero.it', 'pass')
        a.save()
        User.objects.create_user('Paolo Rossi', 'test@danda.com', 'pass')
        User.objects.create_user('Marco Verdi', 'test@danda.com', 'pass')
        User.objects.create_user('Luca Bianchi', 'test@danda.com', 'pass')
        User.objects.create_user('Alvaro Giallo', 'test@danda.com', 'pass')
        r = []
        r.append(Ristorante.objects.create(nome = "Panda", telefono = "049 4432 543", indirizzo = "Via m. Polo, 32"))
        r.append(Ristorante.objects.create(nome = "Giara", telefono = "049 4424 586", indirizzo = "Via g. Verdi, 12"))
        r.append(Ristorante.objects.create(nome = "Lante", telefono = "049 4455 511", indirizzo = "Via Roma, 34/a"))
        for i in piatti:
            print "Creo la portata", i[0]
            p = Portata.objects.create(name = i[0])
            p.save()
            for j in r:
                price = (i[1] + .1*randint(-5, 5))
                print "Per", j, "il piatto", p, "costerà %2.2f Euro" % price
                Piatto.objects.create(portata = p, ristorante = j, prezzo = price)
        