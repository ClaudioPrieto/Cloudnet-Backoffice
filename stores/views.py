from django.shortcuts import render,HttpResponse
from .models import Store
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.

class Store_list(ListView):
    model = Store
    def get_context_data(self, **kwargs):# con este metodo de la clase heredada se puede mandar un contexto normal con cualquier info
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context

class Store_detail(DetailView):
    model = Store

class Store_create(CreateView):
    model = Store
    fields = ['name','description']
    def get_success_url(self):
        return reverse('store-index')
     
    