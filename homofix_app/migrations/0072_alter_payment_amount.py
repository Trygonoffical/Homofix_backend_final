# Generated by Django 4.2 on 2023-06-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homofix_app', '0071_remove_booking_pay_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]