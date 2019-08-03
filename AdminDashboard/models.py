from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
# from EmployeeDashboard.models import EmployeeProfile


# Create your models here.

#ADMIN PROFILE 
class AdminProfile(models.Model):
    user=models.OneToOneField(User)
    image = models.ImageField(upload_to='profile_pics/admin/', blank=True)

    def __str__(self):
         return self.user.username


#admin reminder
class AdminReminder(models.Model):
    admin_name = models.ForeignKey(AdminProfile, on_delete = models.CASCADE, default=1)
    content = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    
    
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.content    

#work assignment to employee
class WorkAssign(models.Model):
    admin_name = models.ForeignKey(AdminProfile, on_delete = models.CASCADE, default=1)
    emp_name=models.ForeignKey('EmployeeDashboard.EmployeeProfile',default=1,on_delete=models.CASCADE)
    work_title=models.CharField(max_length=50)
    work_content=models.CharField(max_length=500)
    work_date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.work_title


#Admin blogging
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class AdminPost(models.Model):
    author = models.ForeignKey(AdminProfile, default=1)
    title=models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    image=models.ImageField(null=True, blank=True,
                            width_field="width_field", 
                            height_field="height_field",
                            upload_to="upload_location")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content=models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AdminDashboard:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp","-updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug= new_slug
    qs = AdminPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=AdminPost)