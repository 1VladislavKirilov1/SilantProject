from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Car
from .forms import CarForm
from .serializers import CarSerializer
from rest_framework import generics


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('car_list')
        else:
            return redirect('car_search_list')


class CarSearchView(ListView):
    model = Car
    template_name = 'vehicles/car_search.html'
    queryset = Car.objects.all()


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'vehicles/car_list.html'

    def get_queryset(self):
        queryset = Car.objects.all()
        if not self.request.user.is_staff:
            user = self.request.user
            try:
                profile = user.userprofile
                if profile.is_service:
                    queryset = queryset.filter(service_company=profile.service_company)
                else:
                    queryset = queryset.filter(client=user)
            except:
                pass
        return queryset


class CarDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'vehicles.view_car'
    model = Car
    template_name = 'vehicles/car_view.html'
    context_object_name = 'obj'


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_car'
    model = Car
    form_class = CarForm
    template_name = 'vehicles/car_create.html'
    success_url = reverse_lazy('car_list')


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_car'
    model = Car
    form_class = CarForm
    template_name = 'vehicles/car_update.html'
    success_url = reverse_lazy('car_list')


class CarDescriptionView(TemplateView):
    template_name = 'services/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = get_object_or_404(Car, pk=self.kwargs["pk"])
        context['attribute'] = 'equipment'
        context['description'] = car.equipment
        return context


class CarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_car'
    model = Car
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'car'
        return context


class CarListAPI(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUserListAPI(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        if isinstance(user, int):
            return Car.objects.filter(client=user)
        else:
            return Car.objects.filter(client__username=user)


class CarDetailAPI(generics.RetrieveAPIView):
    serializer_class = CarSerializer

    def get_object(self):
        return Car.objects.get(pk=self.kwargs['pk'])
