from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path("", views.ProductView.as_view(), name="home"),
    path("search/", views.search_view, name="search"),
    path("<int:pk>/", views.ProductDetail.as_view(), name="detail"),
]
