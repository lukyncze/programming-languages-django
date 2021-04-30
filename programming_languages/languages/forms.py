from django.forms import ModelForm
from .models import *

class JazykyForm(ModelForm):
    class Meta:
        model = Jazyk
        fields = ['nazev', 'popis', 'oblibenost', 'typ', 'foto']