from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('maintenances/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('complaints/', ComplaintListView.as_view(), name='complaint_list'),
    path('car/<pk>/maintenances', MaintenanceCarListView.as_view(), name='car_maintenance'),
    path('car/<pk>/complaints', ComplaintCarListView.as_view(), name='car_complaint'),
    path('maintenance/create', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('complaint/create', ComplaintCreateView.as_view(), name='complaint_create'),
    path('maintenance/<pk>/update', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('complaint/<pk>/update', ComplaintUpdateView.as_view(), name='complaint_update'),
    path('maintenance/<pk>/delete', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('complaint/<pk>/delete', ComplaintDeleteView.as_view(), name='complaint_delete'),
    path('maintenance/<pk>/description/<atribute>', MaintenanceDescriptionView.as_view(), name='maintenance_description'),
    path('complaint/<pk>/description/<atribute>', ComplaintDescriptionView.as_view(), name='complaint_description'),

    path('api/maintenances/',MaintenanceListAPI.as_view(),name='maintenance_list_api'),
    path('api/<user>/maintenances/',MaintenanceUserListAPI.as_view(),name='user_maintenance_list_api'),
    path('api/maintenance/<pk>/',MaintenanceDetailAPI.as_view(),name='maintenance_detail_api'),
    path('api/complaints/',ComplaintListAPI.as_view(),name='complaint_list_api'),
    path('api/<user>/complaints/',ComplaintUserListAPI.as_view(),name='user_complaint_list_api'),
    path('api/complaint/<pk>/',ComplaintDetailAPI.as_view(),name='complaint_detail_api'),
]