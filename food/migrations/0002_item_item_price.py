# Generated by Django 3.2.9 on 2021-11-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
