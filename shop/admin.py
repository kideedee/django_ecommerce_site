from django.contrib import admin

from shop.models import Product, Order

admin.site.site_header = 'E-commerce Site'
admin.site.site_title = 'ABC Shop'
admin.site.index_title = 'Manage ABC Shop'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category', 'description', 'image']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
