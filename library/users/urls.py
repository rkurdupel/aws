from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'), 
    path('personal_info/', views.personal_info, name = "personal_info"),
    path('edit_data/', views.edit_data, name = "edit_data"),
    path('edit_specific_user/<int:user_id>/', views.edit_specific_user, name = 'edit_specific_user'),
    path('<str:first_name>/', views.get_user, name='user'),
    
]
