from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from page1.models import WorkerProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField( required=True )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class meta:
        model = User
        fields = {
            'username'
            'first_name'
            'last_name'
            'phone_number'
            'email'
            'password1'
            'password2'
        }
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']
        user.phone_number= self.cleaned_data['phone_number']

        if commit:
             user.save()
        return user 

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields= (
             'first_name',
             'last_name',
             'email',
             #'phone_number',
        )

class Workersreg(forms.ModelForm):

	class Meta:
		model = WorkerProfile
		fields =(
			'name',
			'category',
			'phone_number',
            'busy'


			
		)
class SelectUser(forms.ModelForm):
    class Meta:
        model=WorkerProfile
        fields=(

            'busy',

            )
