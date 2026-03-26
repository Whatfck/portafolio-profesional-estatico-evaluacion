from django.shortcuts import render

def portfolio(request):
    """Vista para mostrar el portafolio de Dev2"""
    return render(request, "dev2/portfolio.html")
