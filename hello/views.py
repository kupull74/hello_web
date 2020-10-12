from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, Django!")


def responsewithhtml(request):
    data = {'first': 'Sanghun', 'second': 'Oh'} # add
    return render(request, 'hello/responsewithhtml.html', context=data)


def home(request):
    return render(request, 'home.html')


def responsewithhtml(request):

# Modify
    data = {'first': 'Sanghun', 'second': 'Oh'}
    data = dict()
    data['first'] = request.GET['first'];
    data['second'] = request.GET['second']
    return render(request, 'hello/responsewithhtml.html', context=data)


def form(request):
    # add
    return render(request, 'hello/requestform.html')

def template(request):
    return render(request, 'hello/template.html')
    