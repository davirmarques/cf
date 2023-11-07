from django.contrib import admin
from django.urls import path, include # new
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path("",            blog.views.index      ,name="index"),
    path('cronograma1/',blog.views.cronograma1,name='cronograma1'),
    path('cronograma2/',blog.views.cronograma2,name='cronograma2'),
    path('materiais/',  blog.views.materiais,  name='materiais'),
    path('relatorios/', blog.views.relatorios, name='relatorios'),
    path('dashboard/',  blog.views.dashboard,  name='dashboard'),
    


]


