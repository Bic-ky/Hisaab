from django.urls import path, include
from . import views


app_name ='account'

urlpatterns =[
    
    path('login/', views.login, name='login'),
    path('adminDashboard/', views.adminDashboard , name='adminDashboard')

]