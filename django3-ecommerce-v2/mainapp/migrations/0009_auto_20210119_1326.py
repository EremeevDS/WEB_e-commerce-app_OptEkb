# Generated by Django 3.0.8 on 2021-01-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210119_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_discount_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена без скидки'),
        ),
    ]
