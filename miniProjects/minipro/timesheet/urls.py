from django.urls import path

from timesheet import views

app_name='timesheet'
urlpatterns=[
    path('summary',views.TimeSheet.as_view(),name='summary'),
    path('timecard',views.addtimecard,name='timecard'),
    path('total_leaves',views.flaskView,name='total_leaves'),
    path('timecard1',views.create_timecard_with_project,name='timecard1'),
    path('employee',views.GetUsers.as_view(),name='employees'),
    path('employee/<int:pk>',views.GetUsesTimeCard.as_view(),name='employee'),


]