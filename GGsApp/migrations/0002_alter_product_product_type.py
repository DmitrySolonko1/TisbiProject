# Generated by Django 4.1.4 on 2022-12-07 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GGsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productType', to='GGsApp.producttype', verbose_name='Тип товара'),
        ),
    ]