# Generated by Django 3.2.6 on 2021-11-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ManyToManyField(to='orders.Order'),
        ),
    ]