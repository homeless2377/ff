from django.urls import path
from . import views

urlpatterns = [
    
    path("facebook", views.index, name="index"),
    path("homelessworking/table", views.table)
    ]