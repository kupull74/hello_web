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



from django.core.paginator import Paginator
def listwithmongowithpaginator(request):
    data = request.GET.copy()
    with MongoClient('mongodb://172.17.0.1:27017/') as client: # your ip
        mydb = client.mydb
        contact_list = list(mydb.economic.find({})) # get Collection with find()
        paginator = Paginator(contact_list, 10) # Show 15 contacts per page.
        page_number = request.GET.get('page', 1)
        data['page_obj'] = paginator.get_page(page_number)
        return render(request, 'board/listwithrawquerywithpaginator.html', context=data)