# Generated by Django 3.1.6 on 2021-03-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='period_order_value',
            field=models.IntegerField(default=1),
        ),
    ]
