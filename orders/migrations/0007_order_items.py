# Generated by Django 3.2.6 on 2021-11-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(help_text='Y', to='orders.OrderItem'),
        ),
    ]
