# Generated by Django 3.1.4 on 2020-12-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_auto_20201209_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='month',
            field=models.PositiveIntegerField(choices=[(1, 'JANUARY'), (2, 'fEBRUARY'), (3, 'MARCH'), (4, 'APRIL'), (5, 'MAY'), (6, 'JUNE'), (7, 'JULY'), (8, 'AUGUST'), (9, 'SEPTEMBER'), (10, 'OCTOBER'), (11, 'NOVEMBER'), (12, 'DECEMBER')], default=12),
        ),
    ]
