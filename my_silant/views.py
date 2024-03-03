from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from vehicles.models import *
from my_silant.models import *
from my_silant.forms import *
from my_silant.serializers import MaintenanceSerializer, ComplaintSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics


class MaintenanceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'my_silant.view_maintenance'
    model = Maintenance
    template_name = 'services/maintenance_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Maintenance.objects.filter(service_company=profile.service_company)
            except:
                return Maintenance.objects.filter(car__client=user)
        else:
            return Maintenance.objects.all()


class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'my_silant.add_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'services/maintenance_create.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'my_silant.change_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'services/maintenance_update.html'
    success_url = reverse_lazy('maintenance_list')


class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'my_silant.delete_maintenance'
    model = Maintenance
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('maintenance_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'maintenance'
        return context


class ComplaintListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'my_silant.view_complaint'
    model = Complaint
    template_name = 'services/complaint_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = User.objects.get(pk=self.request.user.pk)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Complaint.objects.filter(service_company=profile.service_company)
            except:
                return Complaint.objects.filter(car__client=user)
        else:
            return Complaint.objects.all()


class ComplaintCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'my_silant.add_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'services/complaint_create.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'my_silant.change_complaint'
    model = Complaint
    form_class = ComplaintForm
    template_name = 'services/complaint_update.html'
    success_url = reverse_lazy('complaint_list')


class ComplaintDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'my_silant.delete_complaint'
    model = Complaint
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('complaint_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'сomplaint'
        return context


class MaintenanceCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'my_silant.view_maintenance'
    model = Maintenance
    template_name = 'services/maintenance_car.html'

    def get_queryset(self):
        car = Car.objects.get(pk=self.kwargs["pk"])
        return Maintenance.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.get(pk=self.kwargs["pk"])
        return context


class ComplaintCarListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'my_silant.view_complaint'
    model = Complaint
    template_name = 'services/complaint_car.html'

    def get_queryset(self):
        car = Car.objects.get(pk=self.kwargs["pk"])
        return Complaint.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.get(pk=self.kwargs["pk"])
        return context


class MaintenanceDescriptionView(TemplateView):
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


class ComplaintDescriptionView(TemplateView):
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


# API
class MaintenanceListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()


class MaintenanceUserListAPI(generics.ListAPIView):
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Maintenance.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = Maintenance.objects.filter(car__client__username=user)
        return queryset


class MaintenanceDetailAPI(generics.RetrieveAPIView):
    serializer_class = MaintenanceSerializer

    def get_object(self):
        obj = Maintenance.objects.get(pk=self.kwargs['pk'])
        return obj


class ComplaintListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class ComplaintUserListAPI(generics.ListAPIView):
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Complaint.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = Complaint.objects.filter(car__client__username=user)
        return queryset


class ComplaintDetailAPI(generics.RetrieveAPIView):
    serializer_class = ComplaintSerializer

    def get_object(self):
        obj = Complaint.objects.get(pk=self.kwargs['pk'])
        return obj
