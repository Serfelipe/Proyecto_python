from django import forms

from . import models

# class ProductoCategoriaForm(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()


class TiendaCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.TiendaCategoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = models.Articulo
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "unidad_medida": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "categoria_id": forms.Select(attrs={"class": "form-control"}),
            "fecha_actualizacion": forms.TextInput(attrs={"class": "form-control"}),
        }