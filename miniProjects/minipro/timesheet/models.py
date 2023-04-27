from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime
# Create your models here.
FUNCTION_TYPE=(
    ('DE','Data Engineering'),
    ('SE','Software Engineering'),
    ('TE','Testing'),
    ('DO','DevOps'),
)
FUNCTIONAL_LEADER =(
    ('RK','Ramesh Kumar'),
    ('NI','Naveen Iyer'),
    ('SN','Suresh Nair'),
    ('NV','Nitin Varma'),

)
PROJECT1_TYPE = (
    ('C','Corporate'),
    ('LS','Lending Stream'),
    ('D','Drafty'),

)
TEAM=(
    ('ST1','Sprint Team 1'),
    ('ST2','Sprint Team 2'),
    ('ST3','Sprint Team 3'),
)

MONTH=(
    (1,'JANUARY'),
    (2,'FEBRUARY'),
    (3,'MARCH'),
    (4,'APRIL'),
    (5,'MAY'),
    (6,'JUNE'),
    (7,'JULY'),
    (8,'AUGUST'),
    (9,'SEPTEMBER'),
    (10,'OCTOBER'),
    (11,'NOVEMBER'),
    (12,'DECEMBER'),

)
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=25,null=True,blank=False)
    team=models.CharField(choices=TEAM,default='SE',max_length=25,null=True,blank=False)
    def __str__(self):
        return('{0}'.format(self.name))



class TimeCard(models.Model):
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique_for_month="date_created")

    function=models.CharField(choices=FUNCTION_TYPE,default='DE',max_length=25,null=True,blank=False)
    functional_leader=models.CharField(choices=FUNCTIONAL_LEADER,default='RK',max_length=25,null=True,blank=False)
    leaves=models.PositiveIntegerField(default=0,null=True,)
    project1 = models.CharField(choices=PROJECT1_TYPE,default='C', max_length=25,null=True,blank=False)
    time_project1 = models.PositiveIntegerField(null=True,blank=False)

    total_time=models.PositiveIntegerField(null=True,blank=False)
    month=models.PositiveIntegerField(choices=MONTH,default=12)
    year=models.PositiveIntegerField(blank=False,default=2020)
    @property
    def Month(self):
        if self.date_created:
            return self.date_created.strftime("%B")
        return "No date entry"
    @property
    def Year(self):

        if self.date_created:
            return self.date_created.strftime("%Y")
        return "No date entry"

    def __str__(self):
        return('{0}-{1}'.format(self.date_created,self.user))


    def get_projects(self):
        return self.projects.all().values_list('project',flat=True)


    def get_projects_time(self):
        return self.projects.all().values_list('time_project',flat=True)
    class Meta:
        verbose_name= _('TimeCard')
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        #today=datetime.date.today()
        #self.month=today.month
        #self.year=today.year

        if TimeCard.objects.filter(month=self.month,year=self.year,user=self.user).exists():
            raise ValidationError("Already submitted")

        return super(TimeCard,self).save(*args, **kwargs)

class Project(models.Model):
    project = models.CharField(default='Drafty' ,max_length=25)
    time_project = models.PositiveIntegerField()
    timecard = models.ForeignKey(
        TimeCard,
        related_name='projects', on_delete=models.SET_NULL,
        null=True)



    def __str__(self):
        return self.project