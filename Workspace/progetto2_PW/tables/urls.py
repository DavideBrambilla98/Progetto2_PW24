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
    path('cittadino/<str:paziente>/', searchCittadini, name='listaPers'),

    #percorsi che usano i filtri passati dai link contenuti nella tabella
    path('cittadino/<str:paziente>/', views.linkCittadinoFiltrato, name='listaPers'),
    path('ospedale/<str:codiceOspedale>/', views.linkOspedaleFiltrato, name='listaOsp'),
]
