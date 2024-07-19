from django.urls import path
from . import views as table_views
from django.views.generic import ListView,DetailView
from .models import PatologiaTable

# listview mostra il contenuto del DB sotto forma di lista

# lista delle tabelle | home page
# tabelle singole
urlpatterns = [
    # passa i valori contenuti nel DB alla pagina html in forma di lista
    # è una scorciatoia per non passare da views.py
    path('', ListView.as_view(
        queryset = PatologiaTable.objects.all().order_by("nome"),
        template_name="Patologie.html"), name='listaPat'),
]
