# Generated by Django 4.2.4 on 2023-08-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='https://c0.wallpaperflare.com/preview/109/634/489/apple-watch-3-smartwatch-heart-rate.jpg', max_length=300),
        ),
    ]
