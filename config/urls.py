from django.contrib import admin
from django.urls import path
from jogos.views import lista_jogos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_jogos, name='lista_jogos'),
]