from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

from .models import *

class ThingListView(ListView):
	model = Thing
	
class ThingUpdateView(UpdateView):
	model = Thing
	fields = ["name",]
	success_url = "/"

	#def test_func(self):
	#	object = self.get_object()
	#	return self.request.user == object.owner
	
class ThingCreateView(CreateView):
	model = Thing
	fields = ["name"]
	success_url = "/"

	#def form_valid(self, form):
	#	form.instance.owner = self.request.user
	#	return super().form_valid(form)
	
class ThingDeleteView(DeleteView):
	model = Thing
	success_url = "/"

	#def test_func(self):
	#	object = self.get_object()
	#	return self.request.user == object.owner
	

class StorageListView(ListView):
	model = Storage
	
class StorageUpdateView(UpdateView):
	model = Storage
	fields = ["name",]
	success_url = "/"
	
class StorageCreateView(CreateView):
	model = Storage
	fields = ["name"]
	success_url = "/"
	
class StorageDeleteView(DeleteView):
	model = Storage
	success_url = "/"


class ProductListView(ListView):
	model = Product
	
class ProductCreateView(CreateView):
	model = Product
	fields = ["name",]
	success_url = "/"

class ManufacturerListView(ListView):
		model = Product
		
class ManufacturerCreateView(CreateView):
		model = Product
		fields = ["name",]
		success_url = "/"
		

class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/login"
	
