from django.contrib import admin
from .models import Profile,SecurityEvent
admin.site.register([Profile,SecurityEvent])
