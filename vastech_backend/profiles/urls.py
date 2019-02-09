from django.conf.urls import url
from . import views
app_name = "profile"

urlpatterns = [
    url("profile/<str:username>", views.ProfileDetails.as_view())
]
