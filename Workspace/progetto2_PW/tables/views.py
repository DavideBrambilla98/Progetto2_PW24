from django.shortcuts import render

# Create your views here.

def tabellaSingola(request):
    return render(request, "TabellaSingola.html")
