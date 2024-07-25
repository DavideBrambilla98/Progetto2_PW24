import pandas as pd
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import PatologiaTable, OspedaleTable, CittadinoTable, PatologiaRicoveroTable, RicoveroTable

try:
    import openpyxl
except ImportError:
    print("Il modulo openpyxl non è installato. Installalo con 'pip install openpyxl'.")

def importa_dati_da_excel():
    # Importa i dati delle patologie
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Patologie')
    dati = df.to_dict('records')
    with transaction.atomic():
        for riga in dati:
            patologia, created = PatologiaTable.objects.get_or_create(
                codice=riga['Codice'],
                defaults={
                    'nome': riga['Nome'],
                    'criticita': riga['Criticita'],
                    'cronica': riga['Cronica'],
                    'mortale': riga['Mortale']
                }
            )

    # Importa i dati dei cittadini
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Persone')
    dati = df.to_dict('records')
    with transaction.atomic():
        for riga in dati:
            cittadino, created = CittadinoTable.objects.get_or_create(
                codFiscale=riga['codFiscale'],
                defaults={
                    'cognome': riga['cognome'],
                    'nome': riga['nome'],
                    'nasLuogo': riga['nasLuogo'],
                    'nasRegione': riga['nasRegione'],
                    'nasProv': riga['nasProv'],
                    'nasCap': riga['nasCap'],
                    'dataNascita': riga['dataNascita'],
                    'resLuogo': riga['resLuogo'],
                    'resRegione': riga['resRegione'],
                    'resProv': riga['resProv'],
                    'resCap': riga['resCap'],
                    'indirizzo': riga['indirizzo']
                }
            )

    # Importa i dati degli ospedali
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Ospedali')
    dati = df.to_dict('records')
    with transaction.atomic():
        for riga in dati:
            try:
                direttore_sanitario = CittadinoTable.objects.get(codFiscale=riga['DirettoreSanitario'])
                ospedale, created = OspedaleTable.objects.get_or_create(
                    codiceStruttura=riga['Codicestruttura'],
                    defaults={
                        'denominazioneStruttura': riga['DenominazioneStruttura'],
                        'indirizzo': riga['Indirizzo'],
                        'comune': riga['Comune'],
                        'descrizioneTipoStruttura': riga['DescrizioneTipoStruttura'],
                        'direttoreSanitario': direttore_sanitario
                    }
                )
            except ObjectDoesNotExist:
                print(f"Direttore sanitario non trovato: {riga['DirettoreSanitario']}")

    # Importa i dati dei ricoveri
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Ricoveri')
    dati = df.to_dict('records')
    with transaction.atomic():
        for riga in dati:
            try:
                paziente = CittadinoTable.objects.get(codFiscale=riga['Paziente'])
                ospedale = OspedaleTable.objects.get(codiceStruttura=riga['CodOspedale'])
                ricovero, created = RicoveroTable.objects.get_or_create(
                    codiceRicovero=riga['CodiceRicovero'],
                    defaults={
                        'codiceOspedale': ospedale,
                        'paziente': paziente,
                        'data': riga['Data'],
                        'durata': riga['Durata'],
                        'motivo': riga['Motivo'],
                        'costo': riga['Costo']
                    }
                )
            except ObjectDoesNotExist as e:
                print(f"Errore nell'importazione del ricovero: {e}")

    # Importa i dati delle patologie ricoveri
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='PatologiaRicovero')
    dati = df.to_dict('records')
    with transaction.atomic():
        for riga in dati:
            try:
                ospedale = OspedaleTable.objects.get(codiceStruttura=riga['CodOspedale'])
                ricovero = RicoveroTable.objects.get(codiceRicovero=riga['CodiceRicovero'])
                patologia = PatologiaTable.objects.get(codice=riga['CodPatologia'])
                patologia_ricovero, created = PatologiaRicoveroTable.objects.get_or_create(
                    codOspedale=ospedale,
                    codRicovero=ricovero,
                    codPatologia=patologia
                )
            except ObjectDoesNotExist as e:
                print(f"Errore nell'importazione della patologia ricovero: {e}")

# Esempio di utilizzo
importa_dati_da_excel()
