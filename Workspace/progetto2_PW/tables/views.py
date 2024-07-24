from django.shortcuts import render
from django.db.models import Q
from .models import PatologiaTable, RicoveroTable, OspedaleTable , CittadinoTable

def searchPatologie(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')
    if search_option =='3' or search_option =='4' or search_option =='5' or search_option =='6':
        search_value = '1'

    if search_option and search_value:
        if search_option == '1':
            queryset = PatologiaTable.objects.filter(nome__icontains=search_value)
        elif search_option == '2':
            queryset = PatologiaTable.objects.filter(criticita__icontains=search_value)
        elif search_option == '3':
            queryset = PatologiaTable.objects.filter(Q(cronica__icontains=1) & ~Q(mortale__icontains=1))
        elif search_option == '4':
            queryset = PatologiaTable.objects.filter(~Q(cronica__icontains=1) & Q(mortale__icontains=1))
        elif search_option == '5':
            queryset = PatologiaTable.objects.filter(Q(cronica__icontains=1) & Q(mortale__icontains=1))
        elif search_option == '6':
            queryset = PatologiaTable.objects.filter(~Q(cronica__icontains=1) & ~Q(mortale__icontains=1))
    else:
        queryset = PatologiaTable.objects.all()

    return render(request, 'Patologie.html', {'queryset': queryset})

def searchOspedali(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = OspedaleTable.objects.filter(denominazioneStruttura__icontains=search_value)
        elif search_option == '2':
            queryset = OspedaleTable.objects.filter(comune__icontains=search_value)
        elif search_option == '3':
            queryset = OspedaleTable.objects.filter(direttoreSanitario__icontains=search_value)
    else:
        queryset = OspedaleTable.objects.all()

    return render(request, 'Ospedali.html', {'queryset': queryset})

def searchRicoveri(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = RicoveroTable.objects.filter(paziente__icontains=search_value)
        elif search_option == '2':
            queryset = RicoveroTable.objects.filter(paziente__icontains=search_value)
        elif search_option == '3':
            queryset = RicoveroTable.objects.filter(codiceOspedale__icontains=search_value)
        elif search_option == '4':
            queryset = RicoveroTable.objects.filter(motivo__icontains=search_value)
        elif search_option == '5':
            queryset = RicoveroTable.objects.filter(data__icontains=search_value)
    else:
        queryset = RicoveroTable.objects.all()

    return render(request, 'Ricoveri.html', {'queryset': queryset})

def searchCittadini(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = CittadinoTable.objects.filter(Q(cognome__icontains=1) & ~Q(nomme__icontains=1))
        elif search_option == '2':
            queryset = CittadinoTable.objects.filter(codFiscale__icontains=search_value)
        elif search_option == '3':
            queryset = CittadinoTable.objects.filter(daraNascita__icontains=search_value)
        elif search_option == '4':
            queryset = CittadinoTable.objects.filter(nasLuogo__icontains=search_value)
        elif search_option == '5':
            queryset = CittadinoTable.objects.filter(indirizzo__icontains=search_value)
    else:
        queryset = CittadinoTable.objects.all()

    return render(request, 'Ricoveri.html', {'queryset': queryset})