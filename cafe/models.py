from django.db import models

class Coffee(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    pImage=models.URLField()

    def get_products_by_id(ids):
        return Coffee.objects.filter(id__in =ids)

# Create your models here.
