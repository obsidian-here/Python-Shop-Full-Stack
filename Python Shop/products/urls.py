from django.urls import path
from . import views
# here '.' signifies current folder we do this to ensure 100% that the right views folder is imported


# /products 
# /products/1/details 
# /products/new 
urlpatterns = [
    path('',views.index),
    path('new/',views.new)
]
