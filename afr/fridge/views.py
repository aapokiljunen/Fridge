from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

from .models import *

class ThingListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		return Thing.objects.filter(owner__username=self.request.user)
		
class ThingUpdateView(UserPassesTestMixin, UpdateView):
	model = Thing
	fields = [
		"product", 
		"storage",
		"expiration_date",
		"name", 
		"description",
	]
	success_url = "/"
	
	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['storage'].queryset = Storage.objects.filter(
			owner__username__in =[self.request.user.username]
		)
		form.fields['storage'].required = True
		return form
	
class ThingCreateView(LoginRequiredMixin, CreateView):
	model = Thing
	fields = [
		"product", 
		"storage",
		"expiration_date", 
		"name", 
		"description",
		]
	success_url = "/"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['storage'].queryset = Storage.objects.filter(
			owner__username__in =[self.request.user.username]
		)
		form.fields['storage'].required = True
		return form
	
	
class ThingDeleteView(UserPassesTestMixin, DeleteView):
	model = Thing
	success_url = "/"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	

class StorageListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		return Storage.objects.filter(owner__username=self.request.user)
	
class StorageUpdateView(UserPassesTestMixin, UpdateView):
	model = Storage
	fields = ["name",]
	success_url = "/"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	
class StorageCreateView(LoginRequiredMixin, CreateView):
	model = Storage
	fields = ["name"]
	success_url = "/"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class StorageDetailView(LoginRequiredMixin, DetailView):
	model = Product
	
class StorageDeleteView(UserPassesTestMixin, DeleteView):
	model = Storage
	success_url = "/"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner


class ProductListView(LoginRequiredMixin, ListView):
	model = Product

class ProductDetailView(LoginRequiredMixin, DetailView):
	model = Product
	
class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ["name", "size", "manufacturer",]
	success_url = "/"
	

class ManufacturerListView(LoginRequiredMixin, ListView):
		model = Manufacturer

class ManufacturerDetailView(LoginRequiredMixin, DetailView):
		model = Manufacturer
		
class ManufacturerCreateView(LoginRequiredMixin, CreateView):
		model = Manufacturer
		fields = ["name",]
		success_url = "/"
		
class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/login"
	
