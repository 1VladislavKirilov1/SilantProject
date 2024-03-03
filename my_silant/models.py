from django.db import models
import django.utils
from vehicles.models import Car


class BaseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TypeMaintenance(BaseModel):
    class Meta:
        verbose_name = 'Вид технического обслуживания'
        verbose_name_plural = 'Виды технических обслуживаний'


class Failure(BaseModel):
    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характеры отказа'


class RecoveryMethod(BaseModel):
    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'


class ServiceCompany(BaseModel):
    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class Maintenance(models.Model):
    type = models.ForeignKey(TypeMaintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    date = models.DateField(default=django.utils.timezone.now, verbose_name='Дата проведения ТО')
    operating_time = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    order_number = models.CharField(max_length=20, verbose_name='№ заказ-наряда')
    order_date = models.DateField(default=django.utils.timezone.now, verbose_name='Дата заказ-наряда')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина', related_name='my_silant_maintenance_set')

    def __str__(self):
        return f'{self.date} {self.car}'

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'


class Complaint(models.Model):
    date_failure = models.DateField(default=django.utils.timezone.now, verbose_name='Дата отказа')
    operating_time = models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')
    node_failure = models.ForeignKey(Failure, on_delete=models.CASCADE, verbose_name='Узел отказа')
    description_failure = models.TextField(blank=True, null=True, verbose_name='Описание отказа')
    method_recovery = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    repair_parts = models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')
    date_recovery = models.DateField(default=django.utils.timezone.now, verbose_name='Дата восстановления')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина', related_name='my_silant_complaint_set')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания', null=True, blank=True)

    def __str__(self):
        return f'{self.date_failure} {self.car}'

    def downtime(self):
        deltatime = self.date_recovery - self.date_failure
        return deltatime.days

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
