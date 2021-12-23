from django.contrib import admin
from django_app.models import Home
from django_app.models import Category_Assinaturas, Author_Assinaturas, Cursos


class ExpenseAdmin(admin.ModelAdmin):
    list_display=('title')
    list_per_page = 5

class EmployeeAdmin(admin.ModelAdmin):
   filter_horizontal = ('field',)

class MyModelAdmin(admin.ModelAdmin):
   list_filter = ['field_01', 'field_02']
admin.site.site_header = 'Research Merlin'
admin.site.register(Home)
admin.site.register(Category_Assinaturas)
admin.site.register(Author_Assinaturas)
admin.site.register(Cursos)
#admin.site.register(Assinaturas)