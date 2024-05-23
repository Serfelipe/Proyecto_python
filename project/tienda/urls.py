from django.urls import path

from . import views

app_name = "tienda"

# TiendaCategoria
urlpatterns = [
    path("", views.home, name="home"),
    path("tiendacategoria/create/", views.TiendaCategoriaCreate.as_view(), name="tiendacategoria_create"),
    path("tiendacategoria/list/", views.TiendaCategoriaList.as_view(), name="tiendacategoria_list"),
    path("tiendacategoria/detail/<int:pk>", views.TiendaCategoriaDetail.as_view(), name="tiendacategoria_detail"),
    path("tiendacategoria/update/<int:pk>", views.TiendaCategoriaUpdate.as_view(), name="tiendacategoria_update"),
    path("tiendacategoria/delete/<int:pk>", views.TiendaCategoriaDelete.as_view(), name="tiendacategoria_delete"),
]

# Artículo
urlpatterns += [
    path("articulo/list/", views.ArticuloList.as_view(), name="articulo_list"),
    path("articulo/create/", views.ArticuloCreate.as_view(), name="articulo_create"),
    path("articulo/detail/<int:pk>", views.ArticuloDetail.as_view(), name="articulo_detail"),
    path("articulo/update/<int:pk>", views.ArticuloUpdate.as_view(), name="articulo_update"),
    path("articulo/delete/<int:pk>", views.ArticuloDelete.as_view(), name="articulo_delete"),
]
