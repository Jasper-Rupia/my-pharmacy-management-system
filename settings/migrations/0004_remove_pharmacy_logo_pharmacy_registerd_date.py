# Generated by Django 4.0.5 on 2022-06-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_pharmacy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='logo',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='registerd_date',
            field=models.DateField(auto_now=True),
        ),
    ]