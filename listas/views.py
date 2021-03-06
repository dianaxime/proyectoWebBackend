from django.shortcuts import render
from datetime import date

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
                    'list': True,
                },
                'instance': {
                    'retrieve': 'listas.view_lista',
                    #'retrieve': True,
                    'partial_update': 'listas.change_lista',
                    'aumentar_producto': lambda user, obj, req: user.is_authenticated,
                    'disminuir_producto': lambda user, obj, req: user.is_authenticated,
                    'obtener_listas': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        lista = serializer.save()
        user = self.request.user
        assign_perm('listas.change_lista', user, lista)
        assign_perm('listas.view_lista', user, lista)
        user.save()
        return Response(serializer.data)

    @action(detail=True, url_path='aumentar-producto', methods=['patch'])
    def aumentar_producto(self, request, pk=None):
        lista = self.get_object()
        cantidad = int(request.data.get('cantidad'))
        lista.cantidadLista += cantidad
        lista.save()
        return Response(ListaSerializer(lista).data)

    @action(detail=True, url_path='disminuir-producto', methods=['patch'])
    def disminuir_producto(self, request, pk=None):
        lista = self.get_object()
        cantidad = int(request.data.get('cantidad'))
        lista.cantidadLista -= cantidad
        lista.save()
        return Response(ListaSerializer(lista).data)
    
    @action(detail=False, url_path='obtener-listas', methods=['get'])
    def obtener_listas(self, request, pk=None):
        return Response(ListaSerializer(lista).data for lista in Lista.objects.filter(fechaLista=(date.today().strftime("%Y-%m-%d"))))

