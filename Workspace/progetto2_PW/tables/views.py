from django.shortcuts import render
from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from .models import PatologiaTable, RicoveroTable, OspedaleTable, CittadinoTable

def searchPatologie(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')
    if search_option == '3' or search_option == '4' or search_option == '5' or search_option == '6':
        search_value = '1'

    if search_option and search_value:
        if search_option == '1':
            queryset = PatologiaTable.objects.filter(nome__icontains=search_value).order_by('nome')
        elif search_option == '2':
            queryset = PatologiaTable.objects.filter(criticita__icontains=search_value).order_by('nome')
        elif search_option == '3':
            queryset = PatologiaTable.objects.filter(Q(cronica='1') & ~Q(mortale='1')).order_by('nome')
        elif search_option == '4':
            queryset = PatologiaTable.objects.filter(~Q(cronica='1') & Q(mortale='1')).order_by('nome')
        elif search_option == '5':
            queryset = PatologiaTable.objects.filter(Q(cronica='1') & Q(mortale='1')).order_by('nome')
        elif search_option == '6':
            queryset = PatologiaTable.objects.filter(~Q(cronica='1') & ~Q(mortale='1')).order_by('nome')
    else:
        queryset = PatologiaTable.objects.all().order_by('nome')

    return render(request, 'Patologie.html', {'queryset': queryset})

def searchOspedali(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = OspedaleTable.objects.filter(denominazioneStruttura__icontains=search_value).order_by('denominazioneStruttura')
        elif search_option == '2':
            queryset = OspedaleTable.objects.filter(comune__icontains=search_value).order_by('denominazioneStruttura')
        elif search_option == '3':
            queryset = OspedaleTable.objects.filter(direttoreSanitario__icontains=search_value).order_by('denominazioneStruttura')
        elif search_option == '4':
            queryset = OspedaleTable.objects.filter(codiceStruttura__icontains=search_value).order_by('denominazioneStruttura')
    else:
        queryset = OspedaleTable.objects.all().order_by('denominazioneStruttura')

    return render(request, 'Ospedali.html', {'queryset': queryset})

def searchRicoveri(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = RicoveroTable.objects.annotate(
                paziente_full_name=Concat(
                    'paziente__nome',
                    Value(' '),  # Aggiungi uno spazio tra nome e cognome
                    'paziente__cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '2':
            queryset = RicoveroTable.objects.filter(paziente__codFiscale__icontains=search_value).order_by('paziente__nome')
        elif search_option == '3':
            queryset = RicoveroTable.objects.filter(codiceOspedale__denominazioneStruttura__icontains=search_value).order_by('paziente__nome')
    else:
        queryset = RicoveroTable.objects.select_related('paziente','codiceOspedale').all().order_by('paziente__nome') #paziente è il nome del campo foreignkey diRicoveroTable

    return render(request, 'Ricoveri.html', {'queryset': queryset})

def searchCittadini(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = CittadinoTable.objects.annotate(
                paziente_full_name=Concat(
                    'nome',
                    Value(' '),  # Aggiungi uno spazio tra nome e cognome
                    'cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '2':
            queryset = CittadinoTable.objects.filter(codFiscale__icontains=search_value).order_by('nome')
        elif search_option == '3':
            queryset = CittadinoTable.objects.filter(dataNascita__icontains=search_value).order_by('nome')
        elif search_option == '4':
            queryset = CittadinoTable.objects.filter(nasLuogo__icontains=search_value).order_by('nome')
        elif search_option == '5':
            queryset = CittadinoTable.objects.filter(indirizzo__icontains=search_value).order_by('nome')
    else:
        queryset = CittadinoTable.objects.all().order_by('nome')

    return render(request, 'Cittadini.html', {'queryset': queryset})

def disclaimer(request):
    return render(request, 'disclaimer.html')