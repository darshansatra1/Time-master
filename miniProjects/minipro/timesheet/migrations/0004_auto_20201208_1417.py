# Generated by Django 3.1.4 on 2020-12-08 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timesheet', '0003_auto_20201208_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_month='date_created'),
        ),
    ]
