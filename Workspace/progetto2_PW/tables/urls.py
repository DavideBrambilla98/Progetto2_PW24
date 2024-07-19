from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView
from .models import PatologiaTable
from .models import RicoveroTable

# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
    # passa i valori contenuti nel DB alla pagina html in forma di lista
    # è una scorciatoia per non passare da views.py
    path('patologia/', ListView.as_view(
        queryset = PatologiaTable.objects.all().order_by("nome"),
        template_name="Patologie.html"), name='listaPat'),
    path('', ListView.as_view(
        queryset=RicoveroTable.objects.all().order_by("paziente"),
        template_name="Ricoveri.html"), name='listaRic'),
]
