from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_authors, name="authors"),
    path("create_author/", views.create_author , name="create_author"),
    path("delete_author/<int:pk>", views.delete_author , name="delete_author"),
    path('edit_author/<int:author_id>', views.edit_author, name = "edit_author"),
]
