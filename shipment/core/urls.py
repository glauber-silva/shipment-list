from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShipmentViewSet


shipment_list = ShipmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

shipment_detail = ShipmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^shipments/$', shipment_list, name='shipments-list'),
    url(r'^shipments/(?P<pk>[0-9]+)/$', shipment_detail, name='shipments-detail')
])
