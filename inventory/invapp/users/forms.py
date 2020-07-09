from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		# choose model thats affected (from x.save()) and change the structure required
		model = User
		fields = ['username', 'email', 'password1', 'password2']

