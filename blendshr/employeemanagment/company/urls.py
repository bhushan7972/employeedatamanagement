from django.urls import path
from .views import  companyProfile,dashboard,sep_dashboard
app_name = 'company'

urlpatterns = [

    path('companyProfile', companyProfile, name = 'companyProfile'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('sep_dashboard:<str:depart>', sep_dashboard, name ='sep_dashboard'),


]