# Generated by Django 3.2 on 2023-01-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_order_taxi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]