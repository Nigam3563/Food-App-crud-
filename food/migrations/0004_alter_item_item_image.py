# Generated by Django 3.2.9 on 2021-11-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://farrerpark.thegoodboys.com.sg/wp-content/uploads/2019/11/food-placeholder.jpg', max_length=500),
        ),
    ]