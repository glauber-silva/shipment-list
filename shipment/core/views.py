from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Shipment
from .serializers import ShipmentSerializer


@api_view(['GET', 'POST'])
def shipment_list(request):
    """
    List all shipments, create a new shipment
    """
    if request.method == "GET":
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ShipmentSerializer(data=request.data.get('shipment', {}))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
def shipment_detail(request, pk):
    """
    Get, update or delete a specific task
    """
    try:
        shipment = Shipment.objects.get(pk=pk)
    except Shipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ShipmentSerializer(shipment, data=request.data.get('shipment', {}))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

