# Generated by Django 4.2 on 2023-06-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homofix_app', '0059_alter_invoice_invoice_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_name',
        ),
    ]
