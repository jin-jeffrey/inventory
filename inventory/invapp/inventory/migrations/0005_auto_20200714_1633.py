# Generated by Django 2.2.13 on 2020-07-14 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200709_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_purchased',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_sold',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
