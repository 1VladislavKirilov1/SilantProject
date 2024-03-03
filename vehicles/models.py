from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Technic(BaseModel):
    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class Engine(BaseModel):
    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'


class Transmission(BaseModel):
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


class Bridge(BaseModel):
    class Meta:
        abstract = True
        verbose_name_plural = 'Модели мостов'


class DrivingBridge(Bridge):
    class Meta:
        verbose_name = 'Модель ведущего моста'


class ControlledBridge(Bridge):
    class Meta:
        verbose_name = 'Модель управляемого моста'


class Car(models.Model):
    car_number = models.CharField(unique=True, max_length=12, verbose_name='Зав. № машины')
    technic = models.ForeignKey(Technic, on_delete=models.CASCADE, verbose_name='Модель техники')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engine_number = models.CharField(max_length=12, verbose_name='Зав. № двигателя')
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(max_length=12, verbose_name='Зав. № трансмиссии')
    driving_bridge = models.ForeignKey(DrivingBridge, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    driving_bridge_number = models.CharField(max_length=12, verbose_name='Зав. № ведущего моста')
    controlled_bridge = models.ForeignKey(ControlledBridge, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    controlled_bridge_number = models.CharField(max_length=12, verbose_name='Зав. № управляемого моста')
    delivery_contract = models.CharField(max_length=20, verbose_name='Договор поставки №, дата')
    date_shipment = models.DateField(default=timezone.now, verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=False, verbose_name='Комплектация (доп. опции)', default="Стандарт")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey('my_silant.ServiceCompany', on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.car_number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_service = models.BooleanField(default=False, blank=True, verbose_name='Является сотрудником сервисной компании')
    service_company = models.ForeignKey('my_silant.ServiceCompany', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Сервисная компания')
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
