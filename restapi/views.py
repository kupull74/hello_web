import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("Hello, God~damn~ Django! ...죄송합니다...")

# def taskstring(request):
#     result = 'Rest API stinrg!'
#     return HttpResponse(result, content_type="text/plain")

# def taskxml(request):
#     result = '<employees><employee> \
#     <firstName>John</firstName> <lastName>Doe</lastName> </employee> \
#     <employee> \
#     <firstName>Anna</firstName> <lastName>Smith</lastName></employee> \
#     </employees>'
#     return HttpResponse(result, content_type='text/xml')


# def taskjson(request):
#     result = {"employees":[{"firstName":"John","lastName":"Doe"},
#                            { "firstName":"Anna", "lastName":"Smith" },
#                            { "firstName":"Peter", "lastName":"Jones" }]}           
#     return JsonResponse(result)