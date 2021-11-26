# Generated by Django 3.2.8 on 2021-10-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='名')),
                ('last_name', models.CharField(max_length=255, verbose_name='性')),
                ('age', models.IntegerField(verbose_name='年齢')),
            ],
        ),
    ]
