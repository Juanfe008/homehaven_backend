from django.urls import path, include
from rest_framework import routers
from registros import views

# versiones api
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosView, 'usuarios')

# todo esto genera las consultas POST, GET, PUT, etc
urlpatterns = [
    path('v1/', include(router.urls)),
]