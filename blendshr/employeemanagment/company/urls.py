from django.urls import path
from .views import  companyProfile,dashboard
app_name = 'company'

urlpatterns = [

    path('companyProfile', companyProfile, name = 'companyProfile'),
    path('dashboard', dashboard, name = 'dashboard'),



]