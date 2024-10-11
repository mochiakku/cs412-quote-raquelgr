# File: views.py
# Author: Raquel Gonzalez raquelgr@bu.edu
# Description: view page for the mini_fb website

from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

# ListView to show all profiles on the platform
class show_all_profiles(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'
    
# DetailView to show a single profile page with all its details
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

# CreateView to handle the creation of a new profile
class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    # Define where to redirect after successfully creating a new profile
    def get_success_url(self):
        return reverse('profile-detail', args=[self.object.id])
    
# CreateView to handle the creation of a new status message for a specific profile
class CreateStatusMessageView(CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_message_form.html'

    # Custom method to set the profile for the status message before saving the form
    def form_valid(self, form):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.instance.profile = profile
        return super().form_valid(form)

    # Define where to redirect after successfully creating a status message
    def get_success_url(self):
        return reverse('profile-detail', kwargs={'pk': self.kwargs['pk']})

    # Custom method to add additional context (the profile) to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])  # Add profile to context
        return context
