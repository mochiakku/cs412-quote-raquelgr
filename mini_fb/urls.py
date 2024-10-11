# File: urls.py
# Author: Raquel Gonzalez raquelgr@bu.edu
# Description: file to define the urls for mini_fb

from django.urls import path
from . import views

# create a list of URLs for this app:
urlpatterns = [
     path(r'', views.show_all_profiles.as_view(), name="show_all_profiles"), 
     path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='profile-detail'),
     path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
     path('profile/<int:pk>/create_status_message/', views.CreateStatusMessageView.as_view(), name='create_status_message'),
]