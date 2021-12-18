from django.db import models

# Create your models here.
class Item(models.Model):
   
   #special method
    def __str__(self):
        return self.item_name
    

    #creating attributes
    item_name = models.CharField(max_length=200)
    item_des = models.CharField(max_length=200)
    item_price = models.IntegerField(null=True, blank=True)
    item_image = models.CharField(max_length=500, default='https://farrerpark.thegoodboys.com.sg/wp-content/uploads/2019/11/food-placeholder.jpg')


    def get_absolute_url(self):
        return f"/food/" 