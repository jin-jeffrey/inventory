# Generated by Django 2.2.13 on 2020-07-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(default='', max_length=15),
        ),
    ]
