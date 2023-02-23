from django.db import models
from django.urls import reverse

from users.models import CustomUser


# Create your models here.
class Marketplace(models.Model):
    marketplace_name = models.CharField(max_length=255, verbose_name='Наименование площадки')

    def __str__(self):
        return self.marketplace_name

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = 'Площадки'


class ProductType(models.Model):
    product_name = models.CharField(max_length=155, verbose_name='Тип продукта')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = 'Типы товара'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="images/%Y/%m/%d/", verbose_name='Фото', blank=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, verbose_name="Площадка",
                                    related_name='marketplaceName')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name="Тип товара",
                                    related_name='productType')
    price = models.FloatField(verbose_name="Цена")
    client_nickname = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Владелец",
                                        related_name='user_nickname')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("product_page", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Deal(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Выберите продукт")
    buyer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Выберите покупателя",
                                 related_name='buyer')
    seller_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Выберите продавца",
                                  related_name='seller')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата проведения сделки')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'


class Payment(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE, verbose_name="Номер сделки")
    client_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Номер покупателя")
    price = models.FloatField(verbose_name="Стоимость")
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'