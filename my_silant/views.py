from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from vehicles.models import Car, UserProfile
from my_silant.models import Maintenance, Complaint
from my_silant.forms import MaintenanceForm, ComplaintForm
from my_silant.serializers import MaintenanceSerializer, ComplaintSerializer
from rest_framework import generics


# Mixin для представлений, требующих аутентификации и разрешения
class AuthPermissionMixin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = '/login/'  # URL для перенаправления пользователя на страницу входа
    raise_exception = True  # Возбуждать исключение PermissionDenied, если пользователь не имеет необходимых прав


# Mixin для представлений, отображающих список объектов
class ObjectListView(AuthPermissionMixin, ListView):
    template_name = None  # Шаблон должен быть определен в наследующем классе
    model = None  # Модель должна быть определена в наследующем классе

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            user = self.request.user
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    queryset = queryset.filter(service_company=profile.service_company)
            except UserProfile.DoesNotExist:
                queryset = queryset.filter(car__client=user)
        return queryset


# Mixin для представлений, отображающих детали объекта
class ObjectDetailView(AuthPermissionMixin, DetailView):
    template_name = None  # Шаблон должен быть определен в наследующем классе
    model = None  # Модель должна быть определена в наследующем классе


# Классы представлений для Maintenance
class MaintenanceListView(ObjectListView):
    permission_required = 'my_silant.view_maintenance'
    template_name = 'services/maintenance_list.html'
    model = Maintenance


class MaintenanceCreateView(AuthPermissionMixin, CreateView):
    permission_required = 'my_silant.add_maintenance'
    template_name = 'services/maintenance_create.html'
    form_class = MaintenanceForm
    success_url = reverse_lazy('maintenance_list')
    model = Maintenance


class MaintenanceUpdateView(AuthPermissionMixin, UpdateView):
    permission_required = 'my_silant.change_maintenance'
    template_name = 'services/maintenance_update.html'
    form_class = MaintenanceForm
    success_url = reverse_lazy('maintenance_list')
    model = Maintenance


class MaintenanceDeleteView(AuthPermissionMixin, DeleteView):
    permission_required = 'my_silant.delete_maintenance'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')
    model = Maintenance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'maintenance'
        return context


# Классы представлений для Complaint
class ComplaintListView(ObjectListView):
    permission_required = 'my_silant.view_complaint'
    template_name = 'services/complaint_list.html'
    model = Complaint


class ComplaintCreateView(AuthPermissionMixin, CreateView):
    permission_required = 'my_silant.add_complaint'
    template_name = 'services/complaint_create.html'
    form_class = ComplaintForm
    success_url = reverse_lazy('complaint_list')
    model = Complaint


class ComplaintUpdateView(AuthPermissionMixin, UpdateView):
    permission_required = 'my_silant.change_complaint'
    template_name = 'services/complaint_update.html'
    form_class = ComplaintForm
    success_url = reverse_lazy('complaint_list')
    model = Complaint


class ComplaintDeleteView(AuthPermissionMixin, DeleteView):
    permission_required = 'my_silant.delete_complaint'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('complaint_list')
    model = Complaint

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'сomplaint'
        return context


# Классы представлений для просмотра Maintenance и Complaint по автомобилю
class MaintenanceCarListView(ObjectListView):
    permission_required = 'my_silant.view_maintenance'
    template_name = 'services/maintenance_car.html'
    model = Maintenance

    def get_queryset(self):
        car = Car.objects.get(pk=self.kwargs["pk"])
        return Maintenance.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.get(pk=self.kwargs["pk"])
        return context


class ComplaintCarListView(ObjectListView):
    permission_required = 'my_silant.view_complaint'
    template_name = 'services/complaint_car.html'
    model = Complaint

    def get_queryset(self):
        car = Car.objects.get(pk=self.kwargs["pk"])
        return Complaint.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.get(pk=self.kwargs["pk"])
        return context


# Классы представлений для модального окна с описанием
class MaintenanceDescriptionView(AuthPermissionMixin, TemplateView):
    permission_required = 'my_silant.view_maintenance'
    template_name = 'services/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance = Maintenance.objects.get(pk=self.kwargs["pk"])
        attribute_name = kwargs.get('attribute', None)
        if attribute_name == 'type':
            context['attribute'] = maintenance.type
            context['description'] = maintenance.type.description
        elif attribute_name == 'service_company':
            context['attribute'] = maintenance.service_company
            context['description'] = maintenance.service_company.description
        return context


class ComplaintDescriptionView(AuthPermissionMixin, TemplateView):
    permission_required = 'my_silant.view_complaint'
    template_name = 'services/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complaint = Complaint.objects.get(pk=self.kwargs["pk"])
        attribute = context['attribute']
        if attribute == 'node_failure':
            context['attribute'] = complaint.node_failure
            context['description'] = complaint.node_failure.description
        elif attribute == 'method_recovery':
            context['attribute'] = complaint.method_recovery
            context['description'] = complaint.method_recovery.description
        elif attribute == 'service_company':
            context['attribute'] = complaint.service_company
            context['description'] = complaint.service_company.description
        return context


# API представления
class MaintenanceListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        if isinstance(user, int):
            return Maintenance.objects.filter(car__client=user)
        return Maintenance.objects.filter(car__client__username=user)


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = MaintenanceSerializer

    def get_object(self):
        return Maintenance.objects.get(pk=self.kwargs['pk'])


class ComplaintListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class ComplaintUserListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        if isinstance(user, int):
            return Complaint.objects.filter(car__client=user)
        return Complaint.objects.filter(car__client__username=user)


class ComplaintDetailAPI(generics.RetrieveAPIView):
    serializer_class = ComplaintSerializer

    def get_object(self):
        return Complaint.objects.get(pk=self.kwargs['pk'])
