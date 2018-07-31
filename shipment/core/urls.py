from django.conf.urls import patterns, url

urlpatterns = patterns(
    'shipment.core.views',
    url(r'^shipments/$', 'shipment_list', name='shipment_list'),
    url(r'^shipments/(?P<pk>[0-9]+)$', 'shipment_detail', name='shipment_detail')
)