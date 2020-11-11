from django.urls import path
from . import views

app_name = "tips"

urlpatterns = [
    path("create/<int:pk>/", views.create_tips, name="tip"),
    path("delete/<int:pk>/", views.delete_tips, name="delete"),
]
