# Generated by Django 4.2 on 2023-04-29 08:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homofix_app', '0018_coupon_booking_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('feature_img', models.ImageField(upload_to='Blog/Feature Image')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]