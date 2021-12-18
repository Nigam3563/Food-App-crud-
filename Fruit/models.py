from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)
    fruit_price = models.IntegerField(null=True)
    fruit_quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.fruit_name
