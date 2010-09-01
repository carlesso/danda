from django import forms
from models import Ristorante, Portata

class OrdineForm(forms.Form):
    restourant = forms.ChoiceField(choices = [(i.id, i.nome) for i in Ristorante.objects.all()])
    def __init__(self, initial_data = None, form_model = False, model = None):
        super(OrdineForm, self).__init__(initial_data)
        print "I"
        for i in Portata.objects.all():
            print initial_data
            if initial_data and initial_data[unicode(i.id)]:
                print "check for", i.id, "in", initial_data.keys(), "is", initial_data[str(i.id)]
                val = initial_data[str(i.id)]
            else:
                val = 0
            self.fields[unicode(i.id)] = forms.IntegerField(required = False, initial = val, label = i.name)
