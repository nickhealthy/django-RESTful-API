from django.urls import path
from addresses import views

urlpatterns = [
    path(r'addresses/', views.address_list),
    path(r'addresses/<int:pk>/', views.address_detail)
]