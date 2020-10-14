from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        kstartup = client.kstartup
        result = list(kstartup.kdbCollection.find({}))
        data['page_buse']=result
        
        return render(request, 'kstartup/listwithmongo.html', context=data)
