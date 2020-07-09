from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
	product = models.CharField(max_length = 50, default = '')
	style = models.CharField(max_length = 15, default = '')
	price = models.FloatField(default = '')
	size = models.CharField(max_length = 10, default = '')
	date_purchased = models.DateTimeField(default=timezone.now)
	date_sold = models.DateTimeField(default=timezone.now)
	sold = models.BooleanField(default=False)
	price_sold = models.FloatField(default=0)
	account = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.product

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})