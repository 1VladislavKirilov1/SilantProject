from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', CarSearchView.as_view(), name='car_search_list'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<pk>/detail', CarDetailView.as_view(), name='car_detail'),
    path('car/create', CarCreateView.as_view(), name='car_create'),
    path('car/<pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('car/<pk>/delete', CarDeleteView.as_view(), name='car_delete'),
    path('car/<pk>/description/<atribute>', CarDescriptionView.as_view(), name='car_description'),

    path('api/cars/',CarListAPI.as_view(),name='car_list_api'),
    path('api/<user>/cars/',CarUserListAPI.as_view(),name='user_car_list_api'),
    path('api/car/<pk>/',CarDetailAPI.as_view(),name='car_detail_api'),
]