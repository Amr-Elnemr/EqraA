from django import forms
from .models import User



class EditProfile(forms.ModelForm):
	# FirstName = forms.CharField(label='First Name', max_length=50)
	# LastName = forms.CharField(label='Last Name', max_length=50)
	# OldPassword = forms.CharField(label='Old Password', max_length=50, widget=PasswordInput)
	# NewPassword = forms.CharField(label='New Password', max_length=50)
	class Meta:
		model = User
		fields = ['first_name','last_name','password','username']
	first_name = forms.CharField(label='First Name', max_length=50)
	last_name = forms.CharField(label='Last Name', max_length=50)
	password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)
	username = forms.CharField(label='Last Name', max_length=50)