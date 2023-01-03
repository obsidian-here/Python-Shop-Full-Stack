from django.contrib import admin
from .models import Product, Offer #to import all the features of the product model 


# we need to create a new class called product admin 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Register your models here.
admin.site.register(Offer,OfferAdmin) #NOTE how we add a separate one for Offer module, and we have to import it too (see top 2nd line)
admin.site.register(Product,ProductAdmin) #NOTE: we also passed the class we just created above
# we are using 'admin' object and using attribute 'site' to use method 'register' to pass the class 'Product'
# this tells django that we wanna manage Product in the admin area 