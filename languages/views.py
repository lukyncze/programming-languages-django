from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from languages.models import Jazyk

def index(request):
    return render(request, template_name='index.html')


class JazykyListView(ListView):
    model = Jazyk
    context_object_name = 'jazyky_list'
    template_name = 'list.html'

class JazykyDetailView(DetailView):
    model = Jazyk
    context_object_name = 'jazyky'
    template_name = 'detail.html'

class JazykyCreate(CreateView):
    model = Jazyk
    fields = fields = ['nazev', 'popis', 'oblibenost', 'typ', 'foto']
    initial = {'cena': '500'}

class JazykyUpdate(UpdateView):
    model = Jazyk
    fields = '__all__'

class JazykyDelete(DeleteView):
    model = Jazyk
    success_url = reverse_lazy('list')
