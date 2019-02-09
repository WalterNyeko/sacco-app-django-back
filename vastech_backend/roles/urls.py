from django.conf.urls import url, include
from .views import RolesView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Roles', RolesView)

urlpatterns = [
    url('', include(router.urls))
]
