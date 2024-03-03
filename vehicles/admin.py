from import_export.admin import ImportExportMixin
from import_export import resources
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, User, Technic, Engine, Transmission, DrivingBridge, ControlledBridge, Car


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups')


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class BaseResource(resources.ModelResource):
    class Meta:
        report_skipped = True


class TechnicResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Technic
        fields = ('id', 'name', 'description')


class EngineResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Engine
        fields = ('id', 'name', 'description')


class TransmissionResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Transmission
        fields = ('id', 'name', 'description')


class DrivingBridgeResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = DrivingBridge
        fields = ('id', 'name', 'description')


class ControlledBridgeResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = ControlledBridge
        fields = ('id', 'name', 'description')


class CarResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Car
        fields = (
            'id', 'car_number', 'technic', 'engine', 'engine_number',
            'transmission', 'transmission_number', 'driving_bridge', 'driving_bridge_number',
            'controlled_bridge', 'controlled_bridge_number', 'delivery_contract', 'date_shipment',
            'consignee', 'delivery_address', 'equipment', 'client', 'service_company',
        )


@admin.register(Technic)
class TechnicAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TechnicResource
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Engine)
class EngineAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EngineResource
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Transmission)
class TransmissionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TransmissionResource
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(DrivingBridge)
class DrivingBridgeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DrivingBridgeResource
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(ControlledBridge)
class ControlledBridgeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ControlledBridgeResource
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CarResource
    list_display = (
        'id', 'car_number', 'technic', 'engine', 'transmission',
        'driving_bridge', 'controlled_bridge', 'date_shipment',
        'equipment', 'client', 'service_company',
    )
    search_fields = ('car_number',)
