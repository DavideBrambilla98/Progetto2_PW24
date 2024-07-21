from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView
from .models import PatologiaTable, OspedaleTable
from .models import RicoveroTable
from .views import searchPatologie

# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
    path('patologia/', searchPatologie, name='listaPat'),
    path('', ListView.as_view(
        queryset=RicoveroTable.objects.all().order_by("paziente"),
        template_name="Ricoveri.html"), name='listaRic'),

    path('ospedale/', ListView.as_view(
        queryset=OspedaleTable.objects.all().order_by("denominazioneStruttura"),
        template_name="Ospedali.html"), name='listaOsp'),
]
