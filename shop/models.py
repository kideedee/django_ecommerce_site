from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300, default='https://c0.wallpaperflare.com/preview/109/634/489/apple-watch-3-smartwatch-heart-rate.jpg')

    def __str__(self):
        return self.title
