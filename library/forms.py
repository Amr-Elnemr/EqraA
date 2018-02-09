from django.contrib.auth.models import User
from django import forms
from .models import User

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email', 'password']

###########

class EditProfile(forms.ModelForm):
	# FirstName = forms.CharField(label='First Name', max_length=50)
	# LastName = forms.CharField(label='Last Name', max_length=50)
	# OldPassword = forms.CharField(label='Old Password', max_length=50, widget=PasswordInput)
	# NewPassword = forms.CharField(label='New Password', max_length=50)
	class Meta:
		model = User
		fields = ['first_name','last_name','password','username']
	first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
	last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'last Name','class':'form-control'}))
	username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'username','class':'form-control'}))
	password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'enter your password','class':'form-control'}))
	