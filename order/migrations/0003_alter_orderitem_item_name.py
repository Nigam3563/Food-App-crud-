# Generated by Django 3.2.9 on 2021-11-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_order_number_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_name',
            field=models.CharField(max_length=300, verbose_name='itemname'),
        ),
    ]
