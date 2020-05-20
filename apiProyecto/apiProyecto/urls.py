"""apiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

from usuarios.views import UsuarioViewSet
from clientes.views import ClienteViewSet
from compras.views import CompraViewSet
from empleados.views import EmpleadoViewSet
from facturas.views import FacturaViewSet
from listas.views import ListaViewSet
from ofertas.views import OfertaViewSet
from pedidos.views import PedidoViewSet
from productos.views import ProductoViewSet
from tiendas.views import TiendaViewSet
from valoraciones.views import ValoracionViewSet
from registros.views import RegistroViewSet

router = routers.DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'listas', ListaViewSet)
router.register(r'ofertas', OfertaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'tiendas', TiendaViewSet)
router.register(r'valoraciones', ValoracionViewSet)
router.register(r'registros', RegistroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
]
