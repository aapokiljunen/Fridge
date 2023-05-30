from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
	path('', StorageListView.as_view()),
	path('storage/new', StorageCreateView.as_view()),
	path('storage/<int:pk>', StorageUpdateView.as_view()),
	path('storage/<int:pk>/delete', StorageDeleteView.as_view()),

	path('thing_list', ThingListView.as_view()),
	path('thing/new', ThingCreateView.as_view()),
	path('thing/<int:pk>', ThingUpdateView.as_view()),
	path('thing/<int:pk>/delete', ThingDeleteView.as_view()),
	
	path('product_list', ProductListView.as_view()),
	path('product/new', ProductCreateView.as_view()),
	path('product/<int:pk>', ProductDetailView.as_view()),

	path('manufacturer_list', ManufacturerListView.as_view()),
	path('manufacturer/new', ManufacturerCreateView.as_view()),
	path('manufacturer/<int:pk>', ManufacturerDetailView.as_view()),
	
  	#path('register', RegisterView.as_view()),
	#path('accounts/login/register', RegisterView.as_view()),
	#path('login', LoginView.as_view(next_page="/")),
	#path('accounts/login/', LoginView.as_view(next_page="/")),
	#path('logout', LogoutView.as_view(next_page="/")),    
]	
