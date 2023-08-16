from django.contrib import admin

from shop.models import Product, Order

admin.site.site_header = 'E-commerce Site'
admin.site.site_title = 'ABC Shop'
admin.site.index_title = 'Manage ABC Shop'

admin.site.register(Product)
admin.site.register(Order)
