from django.shortcuts import render

def portfolio(request):
    """Vista para mostrar el portafolio de Dev1"""
    return render(request, "dev1/portfolio.html")
