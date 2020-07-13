from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Item
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.decorators import login_required
# Create your views here.

def about(request):
	return render(request, 'inventory/about.html')

class ItemListView(ListView):
	model = Item
	template_name = 'inventory/home.html'
	context_object_name = 'stock'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.request.user)
		return Item.objects.filter(account=user, sold=False).order_by('product')

class ItemSoldListView(ListView):
	model = Item
	template_name = 'inventory/homeSold.html'
	context_object_name = 'stock'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.request.user)
		return Item.objects.filter(account=user, sold=True).order_by('product')

class ItemDetailView(DetailView):
	model = Item

	def form_valid(self, form):
		form.instance.account = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.account:
			return True
		return False

class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['product', 'color', 'size', 'style', 'price', 'date_purchased']
	success_url = "/inventory" 

	def form_valid(self, form):
		form.instance.account = self.request.user
		return super().form_valid(form)

# Use UserPassesTestMixin if don't want others updating person's project
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item
	success_url = "/inventory"
	fields = ['product', 'color', 'size', 'style', 'price', 'date_purchased', 'date_sold', 'sold', 'price_sold']

	def form_valid(self, form):
		form.instance.account = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.account:
			return True
		return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView,):
	model = Item
	success_url = "/inventory"

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.account:
			return True
		return False