# Generated by Django 4.0.5 on 2022-07-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(max_length=30)),
                ('customer', models.CharField(default='no_name', max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('items', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('trans_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
