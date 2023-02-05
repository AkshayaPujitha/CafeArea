from django.db import models
import datetime
from django.core.validators import MinLengthValidator

class Coffee(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    pImage=models.URLField()

    def get_products_by_id(ids):
        return Coffee.objects.filter(id__in =ids)
class Order(models.Model):
    email=models.EmailField(default="maa@gamil.com")
    product = models.ForeignKey(Coffee,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def order(self):
        self.save()
    def get_orders_by_id(ids):
        return Order.objects.filter(id__in =ids)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False
# Create your models here.
