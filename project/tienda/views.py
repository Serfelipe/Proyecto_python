from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


def home(request):
    return render(request, "tienda/index.html")

class TiendaCategoriaList(ListView):
    model = models.TiendaCategoria

    def get_queryset(self) -> QuerySet:
            if self.request.GET.get("consulta"):
                consulta = self.request.GET.get("consulta")
                object_list = models.TiendaCategoria.objects.filter(nombre__icontains=consulta)
            else:
                object_list = models.TiendaCategoria.objects.all()
            return object_list
    

class TiendaCategoriaCreate(CreateView):
    model = models.TiendaCategoria
    form_class = forms.TiendaCategoriaForm
    success_url = reverse_lazy("tienda:home")


class TiendaCategoriaUpdate(UpdateView):
    model = models.TiendaCategoria
    form_class = forms.TiendaCategoriaForm
    success_url = reverse_lazy("tienda:articulocategoria_list")


class TiendaCategoriaDetail(DetailView):
    model = models.TiendaCategoria


class TiendaCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.TiendaCategoria
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("tienda:articulocategoria_list")


class ArticuloList(ListView):
    model = models.Articulo

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Articulo.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Articulo.objects.all()
        return object_list


class ArticuloCreate(CreateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    success_url = reverse_lazy("tienda:home")


class ArticuloUpdate(UpdateView):
    model = models.Articulo
    form_class = forms.ArticuloForm
    success_url = reverse_lazy("tienda:articulo_list")


class ArticuloDetail(DetailView):
    model = models.Articulo


class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = models.Articulo
    success_url = reverse_lazy("tienda:articulo_list")




