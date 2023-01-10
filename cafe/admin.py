from django.contrib import admin
from .models import Coffee,Order,Customer

class CoffeeAdmin(admin.ModelAdmin):
    list_display=('name','price')
#class CustomerAdmin(admin.ModelAdmin):
  #  list_display=['firstname']

admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(Order)
admin.site.register(Customer)


