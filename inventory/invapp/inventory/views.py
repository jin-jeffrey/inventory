from django.shortcuts import render
from .models import Item
# Create your views here.

def home(request):
	context = {
		'stock': Item.objects.all()
	}
	return render(request, 'inventory/home.html', context)
