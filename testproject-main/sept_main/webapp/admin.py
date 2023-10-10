# In your admin.py file
from django.contrib import admin
from .models import CustomUser  # Import your model

# Register your model with the admin site
admin.site.register(CustomUser)