from django import forms
from timesheet import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.forms import (formset_factory, modelformset_factory)

class TimeCardForm(forms.ModelForm):


    class Meta:
        model =models.TimeCard
        exclude=['user']

ProjectFormset = modelformset_factory(
    models.Project,
    fields=('project','time_project', ),
    extra=1,
    widgets={'project': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Project Name here'
        }),
        'time_project': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Time for Project  here'
        })
    }
)

'''
    def clean(self):
        cleaned_data = self.cleaned_data
        if models.TimeCard.objects.filter(date_created=datetime.now(),user=cleaned_data['user']).exists():
            raise ValidationError('Already Submited')

        # Always return cleaned_data
        return cleaned_data
'''