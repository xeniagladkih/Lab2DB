from django.contrib import admin
from .models import *

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderModel)
admin.site.register(ShippingAddress)