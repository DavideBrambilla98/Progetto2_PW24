from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView
<<<<<<< Updated upstream
from .models import PatologiaTable
=======
from .models import PatologiaTable, OspedaleTable
from .models import RicoveroTable
from .models import PersoneTable
>>>>>>> Stashed changes

# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
    # passa i valori contenuti nel DB alla pagina html in forma di lista
    # è una scorciatoia per non passare da views.py
    path('', ListView.as_view(
        queryset = PatologiaTable.objects.all().order_by("nome"),
        template_name="Patologie.html"), name='listaPat'),
<<<<<<< Updated upstream
=======
    path('', ListView.as_view(
        queryset=RicoveroTable.objects.all().order_by("paziente"),
        template_name="Ricoveri.html"), name='listaRic'),

    path('ospedale/', ListView.as_view(
        queryset=OspedaleTable.objects.all().order_by("denominazioneStruttura"),
        template_name="Ospedali.html"), name='listaOsp'),

    path('persone/', ListView.as_view(
        queryset=PersoneTable.objects.all().order_by("codFiscale"),
        template_name="Persone.html"), name='listaPers'),
>>>>>>> Stashed changes
]
