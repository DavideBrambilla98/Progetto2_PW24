from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView

from .models import PatologiaTable, OspedaleTable
from .models import RicoveroTable
from .views import searchPatologie
from .models import PersoneTable
from .views import RicoveroTableCreate, RicoveroTableDelete, RicoveroTableUpdate


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
        
    path('cittadino/', ListView.as_view(
        queryset=PersoneTable.objects.all().order_by("codFiscale"),
        template_name="cittadini.html"), name='listaPers'),

    path('create/', RicoveroTableCreate.as_view(), name='create'),
    path('update/<int:pk>', RicoveroTableUpdate.as_view(), name='update'),
    path('delete/<int:pk>', RicoveroTableDelete.as_view(), name='delete'),
]
