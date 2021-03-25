from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import company_profile
from .models import companyP
from moderator.models import CustomUser, Profile

from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse


# Create your views here.
@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_company, login_url='moderator:index')
def companyProfile(request):
    company = companyP.objects.get(user=request.user)

    if request.method == 'POST':

        form = company_profile(request.POST, request.FILES, instance=company)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.is_active = True
            userprofile.save()
            return redirect('company:dashboard')
    else:
        form = company_profile()

    return render(request, 'company/profile/create_profile.html', locals())


@login_required(redirect_field_name='/')
@user_passes_test(lambda u: u.is_company, login_url='moderator:index')
def dashboard(request):
    section = 'dashboard'
    hr = companyP.objects.all()
    hr_pro = companyP.objects.filter(department='PRODUCTION')
    hr_sales = companyP.objects.filter(department='SALES')
    hr_marketing = companyP.objects.filter(department='MARKETING')
    hr_hr = companyP.objects.filter(department='HR')
    return render(request, 'company/dashboard.html', locals())

#
# def sep_dashboard(request, depart):
#     section = 'department'
#     manager = managerP.objects.filter(department=depart)
#     employee = employeeP.objects.filter(department=depart)
#     if depart == 'PRODUCTION':
#         return render(request, 'hr/department/productiondep.html', locals())
#     elif depart == 'MARKETING':
#         return render(request, 'hr/department/marketingdep.html', locals())
#     elif depart == 'SALES':
#         return render(request, 'hr/department/salesdep.html', locals())
#     else:
#         hr = companyP.objects.filter(department=depart)
#         return render(request, 'hr/department/hrdep.html', locals())