from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Addresses
from .serializers import AddressesSerializer

# Create your views here.

@csrf_exempt
def address_list(request):
    """
    List all code addresses, or create a new address.
    """
    # Read
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Create
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# 단건조회
@csrf_exempt
def address_detail(request, pk):
    """
    Retrieve, update or delete a code address.
    """
    try:
        address = Addresses.objects.get(pk=pk)
    except Addresses.DoesNotExist:
        return HttpResponse(status=404)

    # Read
    if request.method == 'GET':
        serializer = AddressesSerializer(address)
        return JsonResponse(serializer.data, safe=False)

    # Update
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(address, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # Delete
    elif request.method == 'DELETE':
        address.delete()
        return HttpResponse(status=204)