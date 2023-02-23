from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    status_choice = (
        ('Подтверждён', 'Подтверждён'),
        ('Не подтверждён', 'Не подтверждён')
    )
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    nickname = models.CharField(max_length=255, verbose_name="NickName")
    email = models.EmailField(max_length=221, verbose_name="email")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    status = models.CharField(max_length=255, choices=status_choice, verbose_name='Статус', default='Не подтверждён')

    def __str__(self):
        return self.username
