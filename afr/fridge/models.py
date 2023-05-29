from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
	name = models.CharField(max_length=160)

	def __str__(self):
		return f'{self.name}'

class Product(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(blank=True)
	manufacturer = models.ForeignKey(
		Manufacturer, 
		on_delete=models.CASCADE,
		related_name = 'products',
	)

	def __str__(self):
		return self.name

class Storage(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name		

class Thing(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	#expirition_date  = models.DateTimeField(blank=True, null=True)
	product = models.ForeignKey(
		Product, 
		on_delete=models.CASCADE,
		related_name = 'things',
	)
	storage = models.ForeignKey(
		Storage, 
		on_delete=models.CASCADE,
		related_name = 'things',
	)
	
	#owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.product} in {self.storage}'
