# Generated by Django 4.2 on 2023-06-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homofix_app', '0082_feedback_booking_id_alter_payment_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='support',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
