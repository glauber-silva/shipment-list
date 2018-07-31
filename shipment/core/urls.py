from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import ShipmentViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ShipmentViewSet)

list_actions = {
    'get': 'list',
    'post': 'create'
}

single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    url(r'^', ShipmentViewSet.as_view(list_actions), name="shipments"),
    url(r'^(?P<pk>\d+)$', ShipmentViewSet.as_view(single_actions), name="shipments"),
]
