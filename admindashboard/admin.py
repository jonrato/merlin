from django.contrib import admin
from .models import Users, Assinaturas, Cursos, PostHome
#home_view

admin.site.register(Users)
admin.site.register(Assinaturas)
admin.site.register(Cursos)
admin.site.register(PostHome)