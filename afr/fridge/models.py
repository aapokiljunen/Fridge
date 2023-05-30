from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Manufacturer(models.Model):
	name = models.CharField(max_length=160)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return f'{self.name}'

class Product(models.Model):
	name  = models.CharField(max_length=160)
	size = models.CharField(max_length=20, blank=True)
	description = models.TextField(blank=True)
	manufacturer = models.ForeignKey(
		Manufacturer, 
		on_delete=models.CASCADE,
		related_name = 'products',
	)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class Storage(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name		

class Thing(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	expiration_date  = models.DateField(
		blank=True, 
		null=True
	)
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
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)
	
	#owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.product} in {self.storage}'

	class Meta:
		ordering = ['expiration_date']

	def is_past_due(self):
		return date.today() > self.date

