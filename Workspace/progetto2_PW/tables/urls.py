from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView

from .models import PatologiaTable, OspedaleTable, CittadinoTable
from .models import RicoveroTable
from .views import searchPatologie, searchOspedali, searchRicoveri, searchCittadini
from .models import CittadinoTable


# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
  
    path('patologia/', searchPatologie, name='listaPat'),
    path('ospedale/', searchOspedali, name='listaOsp'),
    path('', searchRicoveri, name='listaRic'),
    path('cittadino/', searchCittadini, name='listaPers'),

    path('create/', table_views.RicoveroTableCreate.as_view(), name='RicCreate'),
    path('update/<int:pk>/', table_views.RicoveroTableUpdate.as_view(), name='RicUpdate'),
    path('delete/<int:pk>/', table_views.RicoveroTableDelete.as_view(), name='RicDelete'),
]
