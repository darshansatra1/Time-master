from django.contrib import admin
from timesheet import models
# Register your models here.
admin.site.register([
    models.TimeCard,
    models.Employee,
    models.Project,
])