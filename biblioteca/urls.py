from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # Adicione esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls'))
    path('auth/', include('usuario.urls'))
    
    
    
]