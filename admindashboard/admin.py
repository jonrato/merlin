from django.contrib import admin
from .models import Users, Assinaturas, Cursos, PostHome,PostQuemSomos, PostNoticias, Dashboard_home, Dashboard_videos
from django_app.models import Post_Assinaturas
#home_view
admin.site.register(Post_Assinaturas)
admin.site.register(Users)
admin.site.register(Assinaturas)
admin.site.register(Cursos)
admin.site.register(PostHome)
admin.site.register(PostQuemSomos)
admin.site.register(PostNoticias)
admin.site.register(Dashboard_home)
admin.site.register(Dashboard_videos)