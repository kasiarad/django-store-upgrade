from django.contrib import admin
from .models import *
from .forms import *



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)





# Register your models here.
