from django.urls import path
from . import views
urlpatterns = [
    path('',views.Question_list,name='Question_list'),
    path('posts/',views.Posts_list,name='Posts'),
    path('users/',views.Users_list,name='users'),
]
