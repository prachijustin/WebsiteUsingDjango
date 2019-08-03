from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404, redirect
from AdminDashboard.forms import (AdminProfileForm, AdminProfileInfoForm, 
                                    EmployeeWorkAssignForm,AdminPostForm,AdminReminderForm)

from EmployeeDashboard.forms import EmployeeProfileForm,EmployeeProfileInfoForm
from django.template import RequestContext
from django.contrib import messages

#imports for login & logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

#imports for blogging
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse,reverse_lazy

from .models import AdminPost,WorkAssign,AdminReminder
from EmployeeDashboard.models import EmployeeProfile,ReportWork
from front.models import Feedback


def test(request):
    return render(request,"test.html")

# Create your views here.
def index(request):
    return render(request,"index.html")

#registration view
def reg(request):
    registered = False
    if request.method == 'POST':
        user_form = AdminProfileForm(data=request.POST)
        profile_form = AdminProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
            return index(request)

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = AdminProfileForm()
        profile_form = AdminProfileInfoForm()

    return render(request,'reg.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered})

#login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/site_admin/dashboard")
            else:
                return HttpResponse("Your account is not active.")

        else:
            print("someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            context={"msg":"Invalid login details supplied"}
            print(context)
            return render(request, 'login.html',context) 
    else:
        return render(request, 'login.html', {})   
        
#decorators for login
@login_required
def special(request):
    return HttpResponse("you are logged in.")


@login_required  
def user_logout(request):
    logout(request)
    return index(request)


#to land on dashboard
def dashboard(request,admin_name=None):
    current_user = request.user.adminprofile
    queryset = AdminReminder.objects.filter(admin_name=current_user)
    emp_len = EmployeeProfile.objects.all()
    emp_length = len(emp_len)
    current_user = request.user.adminprofile
    post_len = AdminPost.objects.filter(author=current_user,draft=False)
    post_length=len(post_len)
    context = {
        "reminder_list": queryset,
        "elength":emp_length,
        "plength":post_length,
    }


    return render(request,'dashboard.html',context)


def add_reminder(request):
    registered = False
    if request.method == 'POST':
        reminder_form = AdminReminderForm(data=request.POST)

        print(reminder_form)
        if reminder_form.is_valid():
            instance=reminder_form.save(commit=False)
            instance.admin_name=request.user.adminprofile
            instance.save()
            registered =True
            return HttpResponseRedirect("/site_admin/dashboard")
        else:
            print(reminder_form.errors)
    else:
        reminder_form = AdminReminderForm()

    return render(request,'dashboard.html',
                        {'reminder_form':reminder_form,
                        'registered':registered})

    



def add_employee(request):
    print("hello")
    registered = False
    if request.method == 'POST':
        emp_form = EmployeeProfileForm(data=request.POST)
        profile_form = EmployeeProfileInfoForm(data=request.POST)
   
        if emp_form.is_valid() and profile_form.is_valid():
            user = emp_form.save(commit=False)
            user.set_password(user.password)
            user.admin_name = request.user.adminprofile
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
            return HttpResponseRedirect("/site_admin/dashboard")

        else:
            print(emp_form.errors,profile_form.errors)

    else:
        emp_form = EmployeeProfileForm()
        profile_form = EmployeeProfileInfoForm()
       

    return render(request,'add_employee.html',
                        {'emp_form':emp_form,
                        'profile_form':profile_form,
                        'registered':registered})

def all_employees(request):
    queryset = EmployeeProfile.objects.all()
    length = len(queryset)
    print(length)
    context = {
        "object_list": queryset,
    }

    return render(request,'all_employees.html',context)


def emp_edit(request, id=None):
    print("hello")
    emp = get_object_or_404(EmployeeProfile, id=id)
   
    if request.method == 'POST':
        profile_form = EmployeeProfileInfoForm(request.POST or None, instance=emp)
        try:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request,'Employee profile is successfully updated')
                return HttpResponseRedirect("/site_admin/dashboard")
            else:
                print(emp_form.errors)
        except Exception as e:
            messages.warning(request,"Employee didn't saved. {}".format(e))
    
    else:
        profile_form = EmployeeProfileInfoForm(instance=emp)

        context = {
            "emp": emp,
            "profile_form": profile_form,
        }
    
    return render(request,"add_employee.html", context)

def emp_delete(request, id=None):
    instance = get_object_or_404(EmployeeProfile, id=id)
    instance.delete()
    return redirect("AdminDashboard:all_employees")    



def assign_work(request):
    queryset = EmployeeProfile.objects.all()
    context = {
        "emp_list": queryset,
    }
    registered = False
    if request.method == 'POST':        
        work_form = EmployeeWorkAssignForm(data=request.POST)
        if work_form.is_valid():
            work_form.save()
            registered = True
            return HttpResponseRedirect("/site_admin/dashboard")
        else:
            print(work_form.errors)
    else:
        work_form = EmployeeWorkAssignForm()
    return render(request,'assign_work.html',
                        {'work_form':work_form,
                        'registered':registered, 
                        "emp_list": queryset})


def work_detail(request, id=None):
    instance = get_object_or_404(WorkAssign, id=id)
    context ={
        "instance":instance,
    }
    return render(request,"work_detail.html",context)


def track_emp_list(request):
    queryset= WorkAssign.objects.all()
    context = {
        "emp_list": queryset,
    }
    return render(request,"track_emp_list.html",context)


def track_emp_detail(request):
    queryset = ReportWork.objects.all()
    context = {
        "emp_list":queryset,
    }
    return render(request,"track_employee.html",context)


def track_emp_reason(request,id=None):
    instance = get_object_or_404(ReportWork, id=id)
    context ={
        "instance":instance,
    }
    
    return render(request,"track_emp_reason.html",context)


#Blogging views
#post creation view
def post_create(request):
    template = 'add_post.html'
    form = AdminPostForm(request.POST or None, request.FILES or None)
    try:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user.adminprofile
            instance.save()
            messages.success(request,'Post created successfully!')
            return HttpResponseRedirect("/site_admin/dashboard")
    except Exception as e:
        messages.warning(request,"Post didn't saved")
    context = {
        "form": form,
    }
    return render(request, template, context)

#list of posts
def post_list(request,author=None):
    current_user = request.user.adminprofile
    queryset = AdminPost.objects.filter(author=current_user)
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request,"all_posts.html",context)


#details of post
def post_detail(request, id=None):
    instance = get_object_or_404(AdminPost, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


#post edit view
def post_update(request, id=None):
    post = get_object_or_404(AdminPost, id=id)

    if request.method == 'POST':
        form = AdminPostForm(request.POST or None, request.FILES or None, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request,'Blog is successfully updated')
                return HttpResponseRedirect("/site_admin/dashboard")
        except Exception as e:
            messages.warning(request,"Post didn't saved. {}".format(e))

    else:
        form = AdminPostForm(instance=post)

        context = {
            'form':form,
            'post':post,
        }
    return render(request, 'add_post.html', context)



#deletion of post
def post_delete(request, id=None):
    instance = get_object_or_404(AdminPost, id=id)
    instance.delete()
    return HttpResponseRedirect("/site_admin/dashboard")


#posts page for users
def all_posts_list(request):
    queryset = AdminPost.objects.filter(draft=False).filter(publish__lte=timezone.now())
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
                ).distinct()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request,"posts_page.html",context)


def feedback(request):
    queryset = Feedback.objects.all()
    context = {
        "object_list": queryset,
    }
    print(queryset)
    return render(request,'feedback.html',context)

def feedback_delete(request, id=None):
    instance = get_object_or_404(Feedback, id=id)
    instance.delete()
    return redirect("AdminDashboard:feedback")    

def feedback_detail(request, id=None):
    instance = get_object_or_404(Feedback, id=id)
    context ={
        "instance":instance,
        "name":instance.name,
        "message":instance.message,
        
    }
    
    return render(request,"feedback_detail.html",context)
