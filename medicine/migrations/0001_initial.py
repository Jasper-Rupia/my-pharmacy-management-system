# Generated by Django 4.0.5 on 2022-07-04 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default', upload_to='uploads/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('generic_name', models.CharField(blank=True, max_length=30)),
                ('quantity', models.IntegerField()),
                ('packaging', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('price', models.IntegerField()),
                ('best_before', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='Available', max_length=30)),
                ('category_name', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='medicine.category')),
            ],
        ),
    ]
