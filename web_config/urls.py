"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restapi import views as restapiview
from hello import views as helloview
#from myhello import views as myhelloview
from board import views as boardview
from kstartup import views as kstartupview
from maps import views as mapsview
from kmountain import views as kmountainview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', restapiview.home, name='home'),
    # path('restapi/task/string', restapiview.taskstring, name='restapi_task_stinrg'),
    # path('restapi/task/xml', restapiview.taskxml, name='restapi_task_xml'),
    # path('restapi/task/json', restapiview.taskjson, name='restapi_task_json'),
    path("hello", helloview.hello, name="hello_home"),
    path("hello/responsewithhtml/", helloview.responsewithhtml),
    path("", helloview.home, name="home"),
    path("home", helloview.home),
    path("hello/form/", helloview.form, name="helloform"),
    path("hello/template/", helloview.template, name="template"),
    path("board/listwithmongo/", boardview.listwithmongo),
    path("kstartup/listwithmongo/", kstartupview.listwithmongo),
    path("board/listwithmongowithpaginator/", boardview.listwithmongowithpaginator),
    path("maps/showmapwithfolium/", mapsview.showmapwithfolium),
    path("kmountain/mountainlist/", kmountainview.mountainlist),
    path("kmountain/home/", kmountainview.home),
    path("kmountain/ms/", kmountainview.ms),
    path("kmountain/housing/", kmountainview.housing),
    path("kmountain/mzoom/", kmountainview.mzoom),
    path('kmountain/ms/mzoom/<int:M_num>/', kmountainview.mzoom, name='mzoom'),
]
