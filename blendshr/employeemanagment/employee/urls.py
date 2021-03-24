
from django.urls import path
from .views import  employeeProfile,dashboard
app_name = 'employee'

urlpatterns = [

    path('employeeProfile', employeeProfile, name = 'employeeProfile'),
    path('dashboard', dashboard, name = 'dashboard'),
    # path('createprofile', create_profile, name = 'createprofile'),
    # path('my_profile', my_profile, name='my_profile'),
    # path('edit_profile', edit_profile, name='edit_profile'),
    # ############  Dashboard Related ##########
    # path('dashboard', dashboard, name='dashboard'),



]