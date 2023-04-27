from django.urls import path

from auth import views

app_name='auth'
urlpatterns =[
    path('login/', views.Login.as_view(),name='login'),
    path('logout/', views.Logout.as_view(),name='logout')
]
