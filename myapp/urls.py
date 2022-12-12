from django.urls import path
from . import views

from django.urls import path
from django.urls import include

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('login',views.login, name='login'),
    path('registro',views.registro, name='registro'),
    path("logout_user", views.logout_user, name="logout_user"),
    path('nosotros',views.nosotros, name='nosotros'),
    path('portafolio',views.portafolio, name='portafolio'),
    path('portafolio/crear',views.crear, name='crear'),
    path('portafolio/editar',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('portafolio/editar/<int:id>',views.editar, name='editar'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)