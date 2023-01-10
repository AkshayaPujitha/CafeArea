from django.db import models
import datetime
class Coffee(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    pImage=models.URLField()

    def get_products_by_id(ids):
        return Coffee.objects.filter(id__in =ids)
class Order(models.Model):
    product = models.ForeignKey(Coffee,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def order(self):
        self.save()

# Create your models here.
