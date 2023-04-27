# Generated by Django 3.1.4 on 2020-12-06 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('function', models.CharField(choices=[('DE', 'Data Engineering'), ('SE', 'Software Engineering'), ('TE', 'Testing'), ('DO', 'DevOps')], max_length=25, null=True)),
                ('functional_leader', models.CharField(choices=[('RK', 'Ramesh Kumar'), ('NI', 'Naveen Iyer'), ('SN', 'Suresh Nair'), ('NV', 'Nitin Varma')], max_length=25, null=True)),
                ('leaves', models.PositiveIntegerField(default=0, null=True)),
                ('project1', models.CharField(choices=[('C', 'Corporate'), ('LS', 'Lending Stream'), ('D', 'Drafty')], max_length=25, null=True)),
                ('time_project1', models.PositiveIntegerField()),
                ('project2', models.CharField(choices=[('C', 'Corporate'), ('LS', 'Lending Stream'), ('D', 'Drafty')], max_length=25, null=True)),
                ('time_project2', models.PositiveIntegerField()),
                ('total_time', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_month='date_created')),
            ],
            options={
                'verbose_name': 'TimeCard',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('team', models.CharField(choices=[('ST1', 'Sprint Team 1'), ('ST2', 'Sprint Team 2'), ('ST3', 'Sprint Team 3')], max_length=25, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
