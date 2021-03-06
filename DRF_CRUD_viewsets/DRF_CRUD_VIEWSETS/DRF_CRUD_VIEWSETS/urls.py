"""DRF_CRUD_VIEWSETS URL Configuration

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
from django.conf.urls import url,include
from testapp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',views.EmployeeCRUD,basename='api')
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include(router.urls)),
    # url('authtoken', views.obtain_auth_token,name='authtoken'),
    # url('jwt', obtain_jwt_token),
    # url('jwt_refresh', refresh_jwt_token),
    # url('jwt_verify', verify_jwt_token),

]