from django import forms
from django.contrib.auth.models import User
from AdminDashboard.models import AdminProfile, WorkAssign, AdminPost, AdminReminder

#admin profile form for User
class AdminProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

#admin profile form for image
class AdminProfileInfoForm(forms.ModelForm):
    class Meta():
        model=AdminProfile
        fields=('image',)


#admin reminder
class AdminReminderForm(forms.ModelForm):
    class Meta():
        model = AdminReminder
        fields=('content',)



#employee work assignment form
class EmployeeWorkAssignForm(forms.ModelForm):
    class Meta():
        model=WorkAssign
        fields=('emp_name','work_title','work_content')





#blogging form for admin
class AdminPostForm(forms.ModelForm):
    class Meta:
        model = AdminPost
        fields = [
            "title",
            "image",
            "content",
            "draft",
            "publish",
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'draft': forms.CheckboxInput(),
            'publish': forms.SelectDateWidget(),
        }
