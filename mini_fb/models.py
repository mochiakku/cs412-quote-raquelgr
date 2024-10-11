# File: models.py
# Author: Raquel Gonzalez raquelgr@bu.edu
# Description: file to define the models for mini_fb

from django.db import models 
from django.utils import timezone  
from django.urls import reverse 

# Define the Profile model, which encapsulates data for each user profile
class Profile(models.Model):
    '''Encapsulate the data for each profile.'''

    # Data attributes for the Profile model
    firstName = models.TextField(blank=False) 
    lastName = models.TextField(blank=False)  
    city = models.TextField(blank=False) 
    email = models.EmailField(blank=False)  
    image_url = models.URLField(blank=False)  
    
    # Define the string representation of the Profile object, useful for admin interface and debugging
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    # Define an accessor method to retrieve all status messages for this profile, ordered by timestamp (most recent first)
    def get_status_messages(self):
        return self.status_messages.all().order_by('-timestamp')

    # Define a method to return the absolute URL for this profile, used for redirection after creating or viewing the profile
    def get_absolute_url(self):
        # The 'profile-detail' pattern is used to generate a URL to show the profile details
        return reverse('profile-detail', args=[str(self.id)])

# Define the StatusMessage model, which represents each status message posted by a user
class StatusMessage(models.Model):
    '''Encapsulates the data for each status message'''

    # Data attributes for the StatusMessage model
    timestamp = models.DateTimeField(default=timezone.now)  
    message = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='status_messages')  

    # Define the string representation of the StatusMessage object
    def __str__(self):
        return f"StatusMessage by {self.profile.firstName} on {self.timestamp}: {self.message}."
