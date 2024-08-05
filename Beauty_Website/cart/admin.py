from django.contrib import admin

from cart.models import Cart,Account,Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Account)