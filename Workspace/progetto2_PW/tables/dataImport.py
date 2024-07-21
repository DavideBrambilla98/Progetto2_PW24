#Classe che serve a importare i valori del DB in excel all'interno del DB sqlite
import pandas as pd
from .models import PatologiaTable
from .models import PatologiaTable, OspedaleTable, PersoneTable
from .models import RicoveroTable
from django.db import transaction

try:
    import openpyxl
except ImportError:
    print("Il modulo openpyxl non è installato. Installalo con 'pip install openpyxl'.")

def importa_dati_da_excel():
    # Leggi il file excel
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Patologie')

    # Crea una lista di dizionari, dove ogni dizionario rappresenta una riga del DataFrame
    dati = df.to_dict('records')

    # Usa una transazione per assicurarti che tutti i dati vengano inseriti correttamente
    with transaction.atomic():
        for riga in dati:
            # Crea un nuovo oggetto PatologiaTable per ogni riga
            patologia = PatologiaTable(
                codice=riga['Codice'],
                nome=riga['Nome'],
                criticita=riga['Criticita'],
                cronica=riga['Cronica'],
                mortale=riga['Mortale']
            )
            # Salva l'oggetto nel database
            patologia.save()

    # Leggi il file excel
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Ricoveri')

    # Crea una lista di dizionari, dove ogni dizionario rappresenta una riga del DataFrame
    dati = df.to_dict('records')

    # Usa una transazione per assicurarti che tutti i dati vengano inseriti correttamente
    with transaction.atomic():
        for riga in dati:
            # Crea un nuovo oggetto PatologiaTable per ogni riga
            ricovero = RicoveroTable(
                codiceOspedale=riga['CodOspedale'],
                codiceRicovero=riga['CodiceRicovero'],
                paziente=riga['Paziente'],
                data=riga['Data'],
                durata=riga['Durata'],
                motivo=riga['Motivo'],
                costo=riga['Costo'],
            )
            # Salva l'oggetto nel database
            ricovero.save()

        # Leggi il file excel
    df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Ospedali')

    # Crea una lista di dizionari, dove ogni dizionario rappresenta una riga del DataFrame
    dati = df.to_dict('records')

    # Usa una transazione per assicurarti che tutti i dati vengano inseriti correttamente
    with transaction.atomic():
        for riga in dati:
            # Crea un nuovo oggetto PatologiaTable per ogni riga
            ospedale = OspedaleTable(
                codiceStruttura=riga['Codicestruttura'],
                denominazioneStruttura=riga['DenominazioneStruttura'],
                indirizzo=riga['Indirizzo'],
                comune=riga['Comune'],
                descrizioneTipoStruttura=riga['DescrizioneTipoStruttura'],
                direttoreSanitario=riga['DirettoreSanitario'],
            )
            # Salva l'oggetto nel database
            ospedale.save()


df = pd.read_excel('../../DB/DataSet.xlsx', sheet_name='Persone')

    # Crea una lista di dizionari, dove ogni dizionario rappresenta una riga del DataFrame
    dati = df.to_dict('records')

    # Usa una transazione per assicurarti che tutti i dati vengano inseriti correttamente
    with transaction.atomic():
        for riga in dati:
            # Crea un nuovo oggetto PatologiaTable per ogni riga
            persona = PersoneTable(
                cognome=riga['cognome'],
                nome=riga['nome'],
                nasLuogo=riga['nasLuogo'],
                nasRegione=riga['nasRegione'],
                nasProv=riga['nasProv'],
                nasCap=riga['nasCap'],
                costo=riga['Costo'],
                dataNascita=riga['dataNascita'],
                codFiscale=riga['codFiscale'],
                resLuogo=riga['resLuogo'],
                resRegione=riga['resRegione'],
                resProv=riga['resProv'],
                resCap=riga['resCap'],
                indirizzo=riga['indirizzo'],

            )
            # Salva l'oggetto nel database
            persona.save()
