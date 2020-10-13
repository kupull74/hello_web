from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://172.17.0.1:27017/') as client:
        mydb = client.mydb
        result = list(mydb.economic.find({}))
        data['page_obj']=result
        
        return render(request, 'board/listwithmongo.html', context=data)
