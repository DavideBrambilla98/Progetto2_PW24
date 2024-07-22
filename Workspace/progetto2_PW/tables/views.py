from django.shortcuts import render
from .models import PatologiaTable
from django.db.models import Q

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

