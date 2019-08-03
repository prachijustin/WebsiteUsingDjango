from django import forms
from . models import Feedback

#admin profile form for User
class FeedbackForm(forms.ModelForm):

    class Meta():
        model=Feedback
        fields=('name','email','message')