from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView




class HomePage(TemplateView):
    template_name = 'homepage.html'





class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> lista de itens do modelo


class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do nosso modelo






# BASED FUNCTION VIEWS

#def homepage(request):
#    return render(request, "homepage.html")


#url - view - html
# def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)