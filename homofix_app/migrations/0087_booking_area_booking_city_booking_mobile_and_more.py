# Generated by Django 4.2 on 2023-12-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homofix_app', '0086_booking_booking_address_booking_booking_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='area',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='zipcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
