# Generated by Django 3.1.2 on 2021-04-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handyman', '0007_user_total_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_hours',
        ),
        migrations.AddField(
            model_name='contract',
            name='total_hours',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
