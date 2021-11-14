from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('addresses.urls'))
]
