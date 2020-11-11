from django.urls import path
from . import views

app_name = "champions"

urlpatterns = [
    path("", views.ChampionView.as_view(), name="champion"),
    path("search/", views.search_view, name="search"),
    path("<int:pk>/", views.ChampionDetailView.as_view(), name="detail"),
]
