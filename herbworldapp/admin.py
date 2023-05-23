from django.contrib import admin


from .models import Customer, Manager, Order, Product

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Order)
admin.site.register(Product)
