# Generated by Django 4.0.5 on 2022-07-04 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='owner',
            field=models.ForeignKey(db_column='owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
