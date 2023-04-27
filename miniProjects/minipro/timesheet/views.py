from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
import requests
import json
from django.views.generic import(
    ListView,
    DetailView)
from timesheet import (
    models,
    forms
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TimeSheet(LoginRequiredMixin,ListView):

    context_object_name = 'timecards'
    template_name = 'timesheet/summary.html'
    login_url= 'auth/login'

    def get_queryset(self):
        return models.TimeCard.objects.filter(user=self.request.user).order_by('-date_created')
'''
class AddTimeCard(View):
    timecardform = forms.TimeCardForm(request.POST)
    def get(self,request):
        context ={
            'timecardform' : timecardform
        }
        return render(request,'timesheet/timecard.html',context)
'''
class GetUsers(UserPassesTestMixin,LoginRequiredMixin,ListView):

    model=models.User
    template_name ='timesheet/user.html'
    def test_func(self):

        if self.request.user.is_superuser:
            return True
        else:
            return False


class GetUsesTimeCard(UserPassesTestMixin,LoginRequiredMixin,DetailView):

    model=models.User
    template_name ='timesheet/time_list.html'

    def test_func(self):

        if self.request.user.is_superuser:
            return True
        else:
            return False

def create_timecard_with_project(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    template_name = 'timesheet/timecard1.html'
    if request.method == 'GET':
        timecardform = forms.TimeCardForm(request.GET or None)
        formset = forms.ProjectFormset(queryset=models.Project.objects.none())
    elif request.method == 'POST':
        timecardform = forms.TimeCardForm(request.POST)
        formset = forms.ProjectFormset(request.POST)
        if timecardform.is_valid() and formset.is_valid():

            timecard = timecardform.save(commit=False)
            user = request.user
            timecard.user = user
            try:
                timecard.save()
            except:
                messages.error(request, 'Time Card Already Submitted for Month')
                return redirect('timesheet:timecard1')

            for form in formset:

                project = form.save(commit=False)
                project.timecard = timecard
                project.save()
            messages.success(request, 'Time Card submitted')
            return redirect('timesheet:summary')
        messages.error(request, 'Failed to submit Time Card')
        return redirect('timesheet:timecard1')

    return render(request, template_name, {
        'timecardform': timecardform,
        'formset': formset,
        'title':'Time Card'
    })

def flaskView(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    if not request.user.is_superuser:
        return redirect('timesheet:timecard')
    template_name ='timesheet/leave.html'
    response=requests.get('http://127.0.0.1:5000/')
    mydict={}


    result=[]
    for ele in response.json():
        result.append((ele["name"],ele["sum(timesheet_timecard.leaves)"]))
    mydict['leaves']=result
    return render(request,template_name,mydict)

def addtimecard(request):

    if not request.user.is_authenticated:
        return redirect('auth:login')

    if request.method =='POST':
        form = forms.TimeCardForm(request.POST)
        if form.is_valid():
            instance =form.save(commit=False)
            user=request.user
            instance.user=user
            try:
                instance.save()
            except:
                messages.error(request, 'Time Card Already Submitted for Month')
                return redirect('timesheet:timecard')

            messages.success(request,'Time Card submitted')
            return redirect('timesheet:summary')
        messages.error(request,'Failed to submit Time Card')
        return redirect('timesheet:timecard')
    dataset=dict()
    form=forms.TimeCardForm()
    dataset['form']=form
    dataset['title']='Time Card'
    return render(request,'timesheet/timecard.html',dataset)




