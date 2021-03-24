

from django.shortcuts import render, redirect
from .forms import employee_profile
from .models import employeeP
from moderator.models import CustomUser, Profile

from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse


# Create your views here.
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_employee, login_url='moderator:index')
def employeeProfile(request):
    employee = employeeP.objects.get(user=request.user)

    if request.method == 'POST':

        form = employee_profile(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('employee:dashboard')
    else:
        form = employee_profile()

    return render(request, 'employee/profile/create_profile.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_employee, login_url='moderator:index')
def dashboard(request):
    section = 'dashboard'
    hr = employeeP.objects.all()
    hr_pro = employeeP.objects.filter(department='PRODUCTION')
    hr_sales = employeeP.objects.filter(department='SALES')
    hr_marketing = employeeP.objects.filter(department='MARKETING')
    hr_hr = employeeP.objects.filter(department='HR')
    return render(request, 'employee/dashboard.html', locals())


