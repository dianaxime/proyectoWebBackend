from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from permisos.services import APIPermissionClassFactory
from compras.models import Compra
from compras.serializers import CompraSerializer

def evaluar(user, obj, request):
    return user.id == obj.idCliente.idUsuario

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CompraPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'compras.view_compra',
                    'partial_update': 'compras.change_compra',
                    'completar': evaluar,
                    'expirar': evaluar,
                    'total': evaluar,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        compra = serializer.save()
        user = self.request.user
        assign_perm('compras.change_compra', user, compra)
        assign_perm('compras.view_compra', user, compra)
        user.save()
        return Response(serializer.data)

    @action(detail=False, url_path='completado', methods=['patch'])
    def completar(self, request, pk=None):
        cliente = request.data.get('idCliente')
        compras = Compra.objects.filter(idCliente=cliente).filter(estadoCompra='activo')
        comprasCompletadas = []
        for compra in compras:
            compra.estadoCompra = 'completado'
            compra.save()
            comprasCompletadas.append(CompraSerializer(compra).data)
        return Response(comprasCompletadas)    

    @action(detail=True, url_path='expirado', methods=['patch'])
    def expirar(self, request, pk=None):
        compra = self.get_object()
        compra.estadoCompra = 'expirado'
        compra.save()
        return Response(CompraSerializer(compra).data)   

    @action(detail=False, url_path='total', methods=['get'])
    def total(self, request, pk=None):
        cliente = request.data.get('idCliente')
        subtotal = Compra.objects.filter(idCliente=cliente).filter(estadoCompra='activo').aggregate(Sum('subtotalCompra'))
        descuento = Compra.objects.filter(idCliente=cliente).filter(estadoCompra='activo').aggregate(Sum('descuentoCompra'))
        subtotal = float(subtotal['subtotalCompra__sum'])
        descuento = float(descuento['descuentoCompra__sum'])
        total = subtotal - descuento
        iva = total * 0.12
        totalFinal = total + iva
        return Response({'subtotal': total, 'iva': iva, 'total': totalFinal})
        