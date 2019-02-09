from django.contrib.auth import get_user_model
from rest_framework import status
from .models import User
from rest_framework.generics import (RetrieveUpdateAPIView,
                                     ListAPIView,
                                     CreateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.views import APIView
import re
# from urllib import request
import json
from .renderers import UserJSONRenderer
from .serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UserSerializer,
    UserWithProfileSerializer,
)
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from password_reset_token.models import Token

from django.utils.timezone import now

import uuid
from vastech_backend.settings import PASSWORD_RESET_LINK


from django.http import HttpResponseRedirect


class RegistrationAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, uidb64, token):
        try:
            email = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(email=email)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            return Response({'message': 'Thank you for your email confirmation. Now you can login your account.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Activation link is invalid!'}, status=status.HTTP_408_REQUEST_TIMEOUT)


class LoginAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def password_reset(request):
    if request.method == 'POST':
        data = {}
        token = uuid.uuid4()

        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
            Token.objects.create(
                token=token,
                email=user.email
            )

            url = PASSWORD_RESET_LINK.format(token)

            message = 'Please click the link to reset your password\n {}'.format(
                url)

            send_mail(
                'Password Reset Link',
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            data['status'] = 1
            data['message'] = "An email has been sent to you, please follow the link in the email to reset your password"

        except User.DoesNotExist:
            data['status'] = 0
            data['message'] = "This email is not registered yet, please sign up instead"
    return Response(data=data)


@api_view(['POST'])
def change_passowrd(request):
    if request.method == 'POST':

        data = {}

        token = request.data.get('token')

        token_object = Token.objects.get(token=token)

        email = token_object.email

        user = User.objects.get(email=email)

        time_created = token_object.created_at

        current_time = now()

        diff = current_time - time_created

        hours = round(diff.total_seconds() / 3600)

        data = {
            'token_status': False
        }

        if token_object:

            data['token_status'] = True

            if hours > 4:

                data['message'] = 'Password reset token only valid for 4 hours, please re-try to reset your password'

            else:

                password = request.data.get('password')

                if validate_password(password) == True:

                    user.set_password(password)

                    user.save()

                    data['message'] = 'Password Successfully Updated!'

                else:

                    data['message'] = 'Password Does Not Meet All Requirements(Must Be At Least 8 Characters, Mixed Capital,Symbols and Lower Cases)'

        else:

            data["message"] = "Token  does not Exist, password reset request denied"

    return Response(data=data)


def validate_password(password):

    return bool(re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password))


class ListUserWithProfiles(ListAPIView):
    queryset = User.objects.all().prefetch_related("profile")
    permission_classes = (IsAuthenticated,)
    serializer_class = UserWithProfileSerializer
