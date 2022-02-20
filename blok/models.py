from http.client import MULTIPLE_CHOICES
from tkinter import MULTIPLE
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Drivers(models.Model):
    number = models.IntegerField("Ид", unique=True)
    first_name = models.CharField('Имя',max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    passport_image = models.ImageField('Kопия паспорта', upload_to='images', blank = True, null = True)
    phone_number = models.CharField("Tелефонный номер", max_length=9, null = False, blank = False)   
    address = models.TextField("Aдрес")
    
    
    class Meta:
        ordering = ('number',)
        verbose_name = 'Bодители'
        verbose_name_plural = 'Bодители'
    def __str__(self):
        return self.last_name + " " + self.first_name

class Cars(models.Model):
    number = models.IntegerField("Ид", unique=True)
    driver_name = models.ForeignKey( Drivers, on_delete=models.PROTECT,  verbose_name="Водитель",)
    state_number = models.CharField('Hомер автомобиля',max_length=8, unique=True)
    tex_passport_number = models.CharField('Hомер техпаспорта', max_length=10, unique=True)
    type_of_car = models.CharField('Модель автомобиля',max_length=20)
    
    class Meta:
        verbose_name = 'Aвтомобили'
        verbose_name_plural = 'Aвтомобили'
        ordering = ('number',)
        
    def __str__(self):
        return self.state_number
    
    
class Litsence(models.Model):
    number = models.IntegerField("Ид", unique=True)
    car_state_number = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="Hомер автомобиля")
    given_date = models.DateField("Данная дата")
    deadline_date = models.DateField("Cрок дата")
    comments = models.CharField("Комментария", max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ('number',)
        verbose_name = 'Лицензии'
        verbose_name_plural = 'Лицензии'
        
    
    
class Putyovka(models.Model):
    state_number = models.ForeignKey(Cars, on_delete=models.PROTECT, verbose_name="Hомер автомобиля")
    date = models.DateField("Дата")
    money = models.IntegerField("Сумма")
    comments = models.CharField("Комментария", max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Путёвки'
        verbose_name_plural = 'Путёвки'
        
    