from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView
from .models import PatologiaTable

# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
    path('',ListView.as_view(
        queryset = PatologiaTable.objects.all().order_by("nome"),
        template_name="ListaTabelle.html"),name='lista'),
    path('tabella-singola/', table_views.tabellaSingola, name='singola'),
]

