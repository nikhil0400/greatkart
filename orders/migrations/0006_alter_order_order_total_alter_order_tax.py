# Generated by Django 4.0.3 on 2022-05-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_address_line_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]