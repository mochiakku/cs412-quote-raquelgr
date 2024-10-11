from django.urls import path
from . import views

# create a list of URLs for this app:
urlpatterns = [
     path(r'', views.show_all_profiles.as_view(), name="show_all_profiles"), 
]