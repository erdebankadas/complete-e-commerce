from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse

#admin.site.register(Product)
#admin.site.register(Category)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','selling_price','discounted_price','brand','product_image','specifications']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity'] 

# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer','product','quantity','order_date','status']#User #Customer

@admin.register(OrderPlaced)
class OrderplacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','customer_info','product','product_info','quantity','order_date','status']

    def customer_info(self,obj):
        link = reverse("admin:grocery_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self,obj):
        link = reverse("admin:grocery_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

admin.site.register(Customer)

@admin.register(ReviewRating)
class ProductReviewModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','subject','review','rating', 'ip', 'status', 'created_at', 'updated_at'] 