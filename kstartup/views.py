from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://192.168.0.134:8088/') as client:
        kstartup = client.kstartup
        result = list(kstartup.kdbCollection.find({}))
        data['page_buse']=result
        
        return render(request, 'kstartup/listwithmongo.html', context=data)
