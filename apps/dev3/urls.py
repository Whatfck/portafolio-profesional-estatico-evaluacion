from django.urls import path
from . import views

app_name = "dev3"

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
]
