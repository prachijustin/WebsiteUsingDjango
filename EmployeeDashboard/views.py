from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from EmployeeDashboard.forms import EmployeeProfileForm,EmployeeProfileInfoForm,ReportWorkInfoForm,EmployeeReminderForm


from django.template import RequestContext

#imports for login & logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required




from .models import EmployeeProfile,EmployeeReminder,ReportWork
from AdminDashboard.models import WorkAssign

# Create your views here.

# EMPlOYEE SECTION  
#login view
def emp_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return employee_dashboard(request)
            else:
                return HttpResponse("Your account is not active.")

        else:
            print("someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'employee_login.html',{}) 

        
#decorators for login
@login_required
def special(request):
    return HttpResponse("you are logged in.")


@login_required  
def user_logout(request):
    logout(request)
    return index(request)
          
     

def employee_dashboard(request,emp_name=None):
    current_user = request.user.employeeprofile
    print(current_user)
    queryset = EmployeeReminder.objects.filter(emp_name=current_user).order_by('-date')

    work_len = WorkAssign.objects.filter(emp_name=current_user)
    wlength=len(work_len)

    report_len = ReportWork.objects.filter(emp_name=current_user)
    rlength=len(report_len)
    context = {
        "reminder_list": queryset,
        "wlength":wlength,
        "rlength":rlength,
    }
    return render(request,"employee_dashboard.html",context)  


def add_reminder(request):
    registered = False
    if request.method == 'POST':
        reminder_form = EmployeeReminderForm(data=request.POST)
        if reminder_form.is_valid():
            instance=reminder_form.save(commit=False)
            instance.emp_name=request.user.employeeprofile
            instance.save()
           
            registered =True
            return HttpResponseRedirect("/employee/employee_dashboard")
        else:
            print(reminder_form.errors)
    else:
        reminder_form = EmployeeReminderForm()

    return render(request,'employee_dashboard.html',
                        {'reminder_form':reminder_form,
                        'registered':registered})




#list of assigned works
def emp_assign_work(request, emp_name=None):
    current_user = request.user.employeeprofile
    queryset = WorkAssign.objects.filter(emp_name=current_user)
    # print(current_user)
    # print(queryset)
    context = {
        "object_list": queryset,
         }
    return render(request,'emp_assign_work.html',context)   

def emp_work_detail(request, id=None):
    instance = get_object_or_404(WorkAssign, id=id)
    context ={
        "instance":instance,
    }
    return render(request,"emp_work_detail.html",context)     


def report_work(request, emp_name=None):
    current_user = request.user.employeeprofile
    queryset = WorkAssign.objects.filter(emp_name=current_user)
    context = {
        "work_list": queryset,
    }
    registered = False
    if request.method == 'POST':
        report_form = ReportWorkInfoForm(data=request.POST)
        if report_form.is_valid():
            instance = report_form.save(commit=False)
            instance.emp_name = current_user
            instance.save()
            registered = True
            return HttpResponseRedirect("/employee/employee_dashboard")
        else:
            print(report_form.errors)
    else:
        report_form = ReportWorkInfoForm()
       
    return render(request,'report_work.html',
                        {'report_form':report_form,
                        'registered':registered, 
                        "work_list": queryset})

