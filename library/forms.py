from django.contrib.auth.models import User
from django import forms
from .models import User, UserProfile

class userform(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput, required=True)
	email=forms.EmailField(widget=forms.EmailInput, required=True)

	class Meta:
		model=User
		fields=['username', 'email', 'password']

###########
class loginform(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput, required=True)
	email=forms.EmailField(widget=forms.EmailInput, required=True)

	class Meta:
		model=User
		fields=['username', 'password']

###########

class EditProfile(forms.ModelForm):
	# FirstName = forms.CharField(label='First Name', max_length=50)
	# LastName = forms.CharField(label='Last Name', max_length=50)
	# OldPassword = forms.CharField(label='Old Password', max_length=50, widget=PasswordInput)
	# NewPassword = forms.CharField(label='New Password', max_length=50)
	class Meta:
		model = User
		fields = ['first_name','last_name','username']
	first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
	last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'last Name','class':'form-control'}))
	username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'username','class':'form-control'}))
	password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'enter your password','class':'form-control'}))
	

##########
#edit profile image
class UpdateProfileImage(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['pic']
	# profile_image = forms.ImageField(label='Profile Image', widget=forms.ClearableFileInput(attrs={'placeholder': 'upload your image','class':'form-control'}))
