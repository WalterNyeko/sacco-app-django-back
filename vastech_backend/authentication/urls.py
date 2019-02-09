from django.conf.urls import url


from .views import (
    UserRetrieveUpdateAPIView,
    RegistrationAPIView,
    LoginAPIView,
    ActivationAPIView,
    ListUserWithProfiles,
)


urlpatterns = [
    url(r'user/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'users/$', RegistrationAPIView.as_view()),
    url(r'^users/login/$', LoginAPIView.as_view()),
    url('users/verify/<uidb64>/<token>',
        ActivationAPIView.as_view(), name='Activation'),
    url(r'users$', ListUserWithProfiles.as_view()),
]
