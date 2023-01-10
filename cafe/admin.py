from django.contrib import admin
from .models import Coffee,Order

class CoffeeAdmin(admin.ModelAdmin):
    list_display=('name','price')
admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(Order)

