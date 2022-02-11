"""netflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie.views import HomePageAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from movie.view_threading_sample import threading_sample_api


schema_view = get_schema_view(
    openapi.Info(
        title="Netflix Application Rest API",
        default_version='v1',
        description='Test description',
        terms_of_service='https://www.google.com',
        contact=openapi.Contact(email='contact@gmail.com'),
        license=openapi.License(name='BSD Licence'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('netflix/', include('movie.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('', HomePageAPIView.as_view()),
    path('threading/', threading_sample_api),
]
