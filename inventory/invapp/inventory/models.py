from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	product = models.CharField(max_length = 50)
	style = models.CharField(max_length = 15, default = 0)
	price = models.FloatField()
	size = models.CharField(max_length = 10)
	date_purchased = models.DateTimeField(default=timezone.now)
	date_sold = models.DateTimeField(default=timezone.now)
	sold = models.BooleanField()

	def __str__(self):
		return self.product