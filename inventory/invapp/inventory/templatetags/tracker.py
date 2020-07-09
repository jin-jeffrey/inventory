from django import template
from ..models import Item
import math

register = template.Library()

@register.simple_tag
def findTotal(firstItem):
	if firstItem != None:
		user = firstItem.account
		Items = Item.objects.filter(account=user)
		total = 0
		for product in Items:
			if product.sold == 0:
				total+=product.price
		return round(total,2)
	return 0

@register.simple_tag
def totalProfit(firstItem):
	if firstItem != None:
		user = firstItem.account
		Items = Item.objects.filter(account=user)
		totalProfit = 0
		for product in Items:
			if product.sold == 1:
				totalProfit += product.price_sold - product.price
		return round(totalProfit,2)
	return 0
	
@register.simple_tag
def profit(item):
	if (item.sold):
		profit = item.price_sold - item.price
		return round(profit,2)

