from django.contrib import admin
from .models import ReleaseCategory, ReleasePost

admin.site.register(ReleasePost)
admin.site.register(ReleaseCategory)