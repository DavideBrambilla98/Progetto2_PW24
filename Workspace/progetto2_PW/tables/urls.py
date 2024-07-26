from django.urls import path
from . import views as table_views, views
from django.views.generic import ListView,DetailView

from .models import PatologiaTable, OspedaleTable, CittadinoTable
from .models import RicoveroTable
from .views import searchPatologie, searchOspedali, searchRicoveri, searchCittadini
from .models import CittadinoTable


# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [

    path('', searchRicoveri, name='listaRic'),
    path('patologia/', searchPatologie, name='listaPat'),
    path('ospedale/', searchOspedali, name='listaOsp'),
    path('cittadino/', searchCittadini, name='listaPers'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
