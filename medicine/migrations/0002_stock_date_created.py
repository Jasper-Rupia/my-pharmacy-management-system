# Generated by Django 4.0.5 on 2022-06-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]