from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_books, name="books"),   
    path("<int:pk>", views.show_book, name="book"),   
    path("specific_user/<int:pk>/", views.show_specific, name="specific"),   
    path("create_book/", views.create_book, name="create_book"),   
    path("update_book/<int:pk>/", views.update_book, name="update_book"),   
]
