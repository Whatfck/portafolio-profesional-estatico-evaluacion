from django.shortcuts import render

def portfolio(request):
    """Vista para mostrar el portafolio de Dev3"""
    return render(request, "dev3/portfolio.html")
