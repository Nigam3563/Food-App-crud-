from django.db import models



# Create your models here)
class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    order_number=models.IntegerField()
    address=models.TextField()
    order_date=models.DateField(verbose_name='OrderDate')

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    item_name=models.CharField(max_length=300,verbose_name='itemname')
    order=models.ForeignKey(Order, verbose_name=("Order"), on_delete=models.CASCADE)
    quantity=models.IntegerField(verbose_name='quantity',default=1)

    def __str__(self):
        return self.item_name
