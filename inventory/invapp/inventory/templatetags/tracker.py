from django import template
from ..models import Item

register = template.Library()

@register.simple_tag
def findTotal():
	total = 0
	for product in Item.objects.all():
		if product.sold == 0:
			total+=product.price
	return total

@register.simple_tag
def totalProfit():
	totalProfit = 0
	for product in Item.objects.all():
		if product.sold == 1:
			totalProfit += product.price_sold - product.price
	return totalProfit

@register.simple_tag
def profit(item):
	if (item.sold):
		profit = item.price_sold - item.price
		return profit

