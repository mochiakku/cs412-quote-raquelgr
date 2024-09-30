from django.urls import path
from . import views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.main, name="main"),
    path(r'order', views.order, name="order"),
    path(r'confirmation', views.confirmation, name="confirmation"),
]