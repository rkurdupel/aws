from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_orders,name="orders"),
    path("create/", views.create_order,name="create_order"),
    path("close/<int:pk>", views.close_order,name="close_order"),
    path("update_order/<int:pk>", views.update_order,name="update_order"),
]
