from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# validate forms	
		if form.is_valid():
			# add user to database
			form.save()

			#redirect to home and display message
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You may log in now.')
			return redirect('login')

	else:
		form = UserRegisterForm()
		
	return render(request, 'users/register.html', {'form': form})
