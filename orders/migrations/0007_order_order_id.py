# Generated by Django 4.0.3 on 2022-05-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_order_total_alter_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]