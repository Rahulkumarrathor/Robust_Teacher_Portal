
from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('add_student/', views.add_student_view, name='add_student'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_student/', views.edit_student_view, name='edit_student'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>/', views.delete_student_view, name='delete'),
]