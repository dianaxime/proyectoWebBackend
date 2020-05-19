from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from productos.models import Producto
from productos.serializers import ProductoSerializer
from ofertas.models import Oferta
from ofertas.serializers import OfertaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ProductoPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': 'productos.view_producto',
                    #'retrieve': lambda user, obj, req: user.is_authenticated,
                    'partial_update': 'productos.change_producto',
                    'aplicar': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        producto = serializer.save()
        user = self.request.user
        assign_perm('productos.change_producto', user, producto)
        assign_perm('productos.view_producto', user, producto)
        user.save()
        return Response(serializer.data)

    @action(detail=True, url_path='aplicar-descuento', methods=['post'])
    def aplicar(self, request, pk=None):
        productos = Producto.objects.all()
        productosDescuento = []
        for producto in productos:
            ofertas = Oferta.objects.filter(idProducto=producto).filter(vencida=False)
            if ofertas.count() > 0:
                producto.descuentoProducto = ofertas.descuentoOferta * producto.precioProducto
            else:
                producto.descuentoProducto = 0
            producto.save()
            productosDescuento.append(ProductoSerializar(producto).data)
        return Response(productosDescuento)    
