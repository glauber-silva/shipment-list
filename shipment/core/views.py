from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Shipment
from .renderers import ShipmentJSONRenderer
from .serializers import ShipmentSerializer


class ShipmentViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    queryset = Shipment.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (ShipmentJSONRenderer,)
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        queryset = self.queryset

        return queryset

    def create(self, request):
        serializer_data = request.data.get('shipment', {})

        serializer = self.serializer_class(
            data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Shipment.DoesNotExist:
            raise NotFound("A shipment with this id does not exist")

        serializer = self.serializer_class(
            serializer_instance, context=serializer_context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=pk)
        except Shipment.DoesNotExist:
            raise NotFound('A shipment with this id does not exist.')

        serializer_data = request.data.get('shipment', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)