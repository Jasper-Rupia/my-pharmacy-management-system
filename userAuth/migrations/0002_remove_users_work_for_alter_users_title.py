# Generated by Django 4.0.5 on 2022-06-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='work_for',
        ),
        migrations.AlterField(
            model_name='users',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]