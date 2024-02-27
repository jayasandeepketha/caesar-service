#from django.shortcuts import render
from django.http import JsonResponse

def greetings(request):
    result = {"message": "Welcome to ciphers service"}
    return JsonResponse(result)

def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    ciphers = caesar_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})

# Create your views here.
