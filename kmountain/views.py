from django.shortcuts import render
import folium
from pymongo import MongoClient
from django.core.paginator import Paginator
import requests
from urllib import parse


def home(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mountaindb = client.mountaindb
        #result = list(mountaindb.mtdbColl.find({}))
        #data['page_buse']=result
        
        return render(request, 'kmountain/home.html', context=data)


def ms(request):
    center = [37.541, 126.986]
    m = folium.Map(center, zoom_start=7)
    data = request.GET.copy()

    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mountaindb = client.mountaindb
        #mt_data_list = list(mountaindb.mtdbColl.find({}))
        result = list(mountaindb.mtdbColl.find({}))
        # data['page_buse']=result
        for mt_data in result:
            lat_lon = [mt_data['M_lat'], mt_data['M_long']]
            pop_text = folium.Html(
                f"Mountain : {mt_data['M_name']}<br>" +
                f"Height : {mt_data['M_height']}<br>" +
                f"Weather : {mt_data['M_weather']}<br>" +
                f"Address : {mt_data['M_address']}<br>", script=True
            )
            pop_up = folium.Popup(pop_text)
            folium.CircleMarker(lat_lon, popup=pop_up, tooltip=mt_data['M_name'], color='red', fill=True, fill_color='green').add_to(m)

        paginator = Paginator(result, 10) # Show 15 contacts per page.

        page_number = request.GET.get('page', 1)
        # page_number = page_number if page_number else 1 

        m = m._repr_html_()
        data = {'page_buse' : result, 'mountain_map' : m, 'page_obj': paginator.get_page(page_number)}
    return render(request, 'kmountain/ms.html', context=data)

###############################
    # data = request.GET.copy()
    # with MongoClient('mongodb://127.0.0.1:27017/')  as client:
    #     mydb = client.mydb
    #     contact_list = list(mydb.economic.find({}))			# get Collection with find()
    #     for info in contact_list:						# Cursor
    #         print(info)

    # paginator = Paginator(contact_list, 10) # Show 15 contacts per page.

    # page_number = request.GET.get('page', 1)
    # # page_number = page_number if page_number else 1 
    # data['page_obj'] = paginator.get_page(page_number)

    # for row in data['page_obj']:
    #     print(f"{row['title']}, {row['link']}")

    # return render(request, 'board/listwithrawquerywithpaginator.html', context=data)
##############################
    
# def ms(request):
#     center = [37.541, 126.986]
#     m = folium.Map(center, zoom_start=7)
#     lat_long = [35.3369, 127.7306]
#     m = folium.Map(lat_long, zoom_start=7.5)
#     popText = folium.Html('<b>Jirisan National Park</b></br>'+str(lat_long), script=True)
#     popup = folium.Popup(popText, max_width=2650)
#     #folium.RegularPolygonMarker(location=lat_long, popup=popup).add_to(m)
#     folium.CircleMarker(location=[35.3369, 127.7306], radius=20, popup=popup, color='red', fill=True, fill_color='green').add_to(m)
#     m = m._repr_html_() # updated
#     datas = {'mountain_map': m}
#     return render(request, 'kmountain/ms.html', context=datas)
        




def mountainlist(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mountaindb = client.mountaindb
        result = list(mountaindb.mtdbColl.find({}))
        data['page_buse']=result
        
        paginator = Paginator(result, 10) # Show 15 contacts per page.
        page_number = request.GET.get('page', 1)
        # page_number = page_number if page_number else 1 
        #m = m._repr_html_()
        data = {'page_buse' : result, 'page_obj': paginator.get_page(page_number)}
    return render(request, 'kmountain/mountainlist.html', context=data)

# def mountainlist(request):
#     data = request.GET.copy()
#     with MongoClient('mongodb://127.0.0.1:27017/') as client:
#         mountaindb = client.mountaindb
#         result = list(mountaindb.mtdbColl.find({}))
#         data['page_buse']=result
#         return render(request, 'kmountain/mountainlist.html', context=data)

def housing(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mountaindb = client.mountaindb
        #result = list(mountaindb.mtdbColl.find({}))
        #data['page_buse']=result
        
        return render(request, 'kmountain/housing.html', context=data)