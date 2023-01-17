"""uber_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import permissions

from accounts import views as acc_view
from rest_framework.routers import DefaultRouter
from service import views as serv_view
from service import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Question Answer Clone API",
      default_version='v-0,02-alpha',
      description="Api для взоимодействия с ВопросыОтветы Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="miko.abidinov@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

service_router = DefaultRouter()
service_router.register('taxi', serv_view.TaxiViewSet)

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/taxi/', views.TaxiViewSet.as_view({'get': 'list'})),
    path('api/taxi/<int:pk>/', views.TaxiRetrieveUpdateDestroyApiView.as_view()),
    path('api/taxi/<int:pk>/order/', views.OrderViewSet.as_view()),
    path('api/taxi/<int:pk>/order/<int:id>/', views.OrderRetrieveUpdateDestroyApiView.as_view()),

    path('api/accounts/', include(acc_router.urls)),
    path('api/service/', include(service_router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
