from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from listas.models import Lista
from listas.serializers import ListaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ListaPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'listas.change_lista',
                    'partial_update': 'listas.change_lista',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        lista = serializer.save()
        user = self.request.user
        assign_perm('listas.change_usuario', user, lista)
        assign_perm('listas.view_usuario', user, lista)
        return Response(serializer.data)

    @action(detail=True, url_path='aumentar-producto', methods=['post'])
    def aumentar_producto(self, request, pk=None):
        lista = self.get_object()
        self.producto_aumentar(lista)
        return Response(ListaSerializer(lista).data)

    def producto_aumentar(self, lista):
        lista.cantidadLista += 1
        lista.save()

    @action(detail=True, url_path='aumentar-producto', methods=['post'])
    def disminuir_producto(self, request, pk=None):
        lista = self.get_object()
        self.producto_disminuir(lista)
        return Response(ListaSerializer(lista).data)

    def producto_disminuir(self, compra):
        lista.cantidadLista -= 1
        lista.save()
