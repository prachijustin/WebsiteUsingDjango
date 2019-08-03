from django.shortcuts import render
from AdminDashboard.models import AdminPost
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from front.forms import FeedbackForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    queryset=AdminPost.objects.filter(draft=False).filter(publish__lte=timezone.now())[:5]
    context={
    "object_list":queryset,
    "title":"List"
    }
    
    return render(request,"index.html",context)
   
def new1(request):
    return render(request,"new1.html")

def new2(request):
    return render(request,"new2.html")    

def new3(request):
    return render(request,"new3.html")

def new4(request):
    return render(request,"new4.html")

def new5(request):
    return render(request,"new5.html")

def new7(request):
    return render(request,"new7.html")   

def new8(request):
    return render(request,"new8.html")    

def new9(request):
    return render(request,"new9.html")

def new10(request):
    return render(request,"new10.html")    


def about(request):
    return render(request,"about.html")          

def post_detail(request, id=None):
    instance = get_object_or_404(AdminPost, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def feedback(request):
    
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        

        if feedback_form.is_valid():
            feedback_form.save()
            return HttpResponseRedirect("/")

        else:
            print(feedback_form.errors)

    else:
        feedback_form = FeedbackForm()
       

    return render(request,'index.html',
                        {'feedback_form':feedback_form})
