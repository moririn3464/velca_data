# Generated by Django 3.2.8 on 2022-02-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_personal',
            name='player_birthday',
            field=models.DateField(auto_now=True),
        ),
    ]