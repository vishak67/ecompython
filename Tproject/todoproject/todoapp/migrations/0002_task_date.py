# Generated by Django 3.2.8 on 2021-10-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-01-04'),
            preserve_default=False,
        ),
    ]