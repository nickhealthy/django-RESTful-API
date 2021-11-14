from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from addresses import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'addresses/', views.address_list),
    path(r'addresses/<int:pk>/', views.address_detail),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
