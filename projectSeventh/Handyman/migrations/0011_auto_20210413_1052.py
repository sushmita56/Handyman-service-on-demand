# Generated by Django 3.1.2 on 2021-04-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handyman', '0010_auto_20210413_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='total_hours',
            field=models.IntegerField(null=True),
        ),
    ]
