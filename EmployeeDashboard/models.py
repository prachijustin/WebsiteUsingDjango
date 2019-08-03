from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from AdminDashboard.models import AdminProfile
# from RayAdvisors.AdminDashboard.models import AdminProfile

# Create your models here.
#EMPLOYEE PROFILE
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User)
    admin_name = models.ForeignKey('AdminDashboard.AdminProfile',default=1)
    email = models.EmailField(max_length=50,default=None)
    emp_name = models.CharField(max_length=30)
    contact_no = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics/employee/', blank=True)  

    def __str__(self):
         return self.user.username

    def get_absolute_url(self):
        return reverse("AdminDashboard:emp_edit", kwargs={"id": self.id})
 

class EmployeeReminder(models.Model):
    emp_name = models.ForeignKey(EmployeeProfile, on_delete = models.CASCADE, default=1)
    content = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ["-date"]



#reporting of work
class ReportWork(models.Model):
    admin_name = models.ForeignKey('AdminDashboard.AdminProfile', on_delete = models.CASCADE, default=1)
    emp_name = models.ForeignKey('EmployeeProfile', on_delete = models.CASCADE, default=1)
    work_title=models.ForeignKey('AdminDashboard.WorkAssign',default=1,on_delete=models.CASCADE,related_name='ewtitle')
    work_progress=models.CharField(max_length=20)
    reason=models.TextField(blank=True,default=None)
    report_date=models.DateField(default=timezone.now)

    def __unicode__(self):
        return self.work_progress

    def __str__(self):
        return self.work_progress