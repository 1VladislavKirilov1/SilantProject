from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources


def create_admin_resource(model_class):
    class_name = f"{model_class.__name__}Admin"

    class Resource(resources.ModelResource):
        class Meta:
            model = model_class
            report_skipped = True
            fields = '__all__'

    admin_class = type(class_name, (ImportExportMixin, admin.ModelAdmin), {
        'resource_class': Resource,
        'list_display': [field.name for field in model_class._meta.fields],
        'filter': [field.name for field in model_class._meta.fields if field.name != 'id'],
    })
    return admin_class


admin.site.register(TypeMaintenance, create_admin_resource(TypeMaintenance))
admin.site.register(Failure, create_admin_resource(Failure))
admin.site.register(RecoveryMethod, create_admin_resource(RecoveryMethod))
admin.site.register(ServiceCompany, create_admin_resource(ServiceCompany))
admin.site.register(Maintenance, create_admin_resource(Maintenance))
admin.site.register(Complaint, create_admin_resource(Complaint))
