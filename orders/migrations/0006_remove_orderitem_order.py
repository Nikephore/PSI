# Generated by Django 3.2.6 on 2021-11-28 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20211128_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]
