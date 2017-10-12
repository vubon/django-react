"""jwtTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from rest_framework import status, serializers, views
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class MessageSerialiser(serializers.Serializer):
    message = serializers.CharField()


class EchoView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = MessageSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(request.data, status=status.HTTP_201_CREATED)


urlpatterns = [
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),

    url(r'^api/$',get_schema_view()),
    url(r'^api/auth/',include('rest_framework.urls', namespace='rest_frameworks')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    url(r'^api/echo/$', EchoView.as_view()),
    url(r'^admin/', admin.site.urls),
]
