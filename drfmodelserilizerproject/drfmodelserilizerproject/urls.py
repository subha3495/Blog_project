"""drfmodelserilizerproject URL Configuration

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
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', views.EmployeeLISTAPIView.as_view()),
    # path('api/create/',views.EmployeeCreateAPIView.as_view()),
    # path('api/<int:pk>/', views.EmployeeRetrieveAPIView.as_view()),
    # path('update/<int:id>/', views.EmployeeUpdateAPIView.as_view()),
    # path('delete/<int:id>/', views.EmployeeDestroyAPIView.as_view()),
    # path('apii/', views.EmployeeListCreateAPIView.as_view()),
    # path('api/<int:id>/', views.EmployeeRetriveUpdateAPIView.as_view()),
    # path('api/<int:id>/', views.EmployeeRetriveDestroyAPIView.as_view()),
    # path('api/<int:id>/', views.EmployeeRetriveUpdateDestroyAPIView.as_view()),
    path('api/', views.EmployeeListCreateModelmixins.as_view()),
    path('api/<int:pk>', views.EmployeeRetriveUpdateDestroyModelmixins.as_view()),

]
