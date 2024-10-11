# File: admin.py
# Author: Raquel Gonzalez raquelgr@bu.edu
# Description: admin file

from django.contrib import admin
from .models import Profile, StatusMessage

admin.site.register(Profile)
admin.site.register(StatusMessage)