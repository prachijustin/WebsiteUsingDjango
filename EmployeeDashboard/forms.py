from django import forms
from django.contrib.auth.models import User
from EmployeeDashboard.models import EmployeeProfile,ReportWork,EmployeeReminder

#employee profile form
class EmployeeProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model=User
        fields=('username','password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

#employee profile form for extra fields
class EmployeeProfileInfoForm(forms.ModelForm):
    class Meta():
        model = EmployeeProfile
        fields = ('emp_name','email','contact_no','location','image')
        widgets = {
            'emp_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact_no': forms.NumberInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }


class EmployeeReminderForm(forms.ModelForm):
    class Meta():
        model = EmployeeReminder
        fields=('content',)



#employee work reporting form
class ReportWorkInfoForm(forms.ModelForm):
    class Meta():
        model=ReportWork
        fields=('work_title','work_progress','reason')        


