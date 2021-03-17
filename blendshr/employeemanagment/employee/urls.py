
from django.urls import path,include
from .views import index
appname='employee'
urlpatterns = [

    path('',index,name='index'),
]
