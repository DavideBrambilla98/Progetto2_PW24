# tables/management/commands/importa_dati.py
from django.core.management.base import BaseCommand
from tables.dataImport import importa_dati_da_excel  # Assicurati che questo import sia corretto

class Command(BaseCommand):
    help = 'Importa i dati da Excel'

    def handle(self, *args, **kwargs):
        importa_dati_da_excel()