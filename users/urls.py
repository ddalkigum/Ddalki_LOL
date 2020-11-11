from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao_callback"),
    path("signup/", views.UserSignupView.as_view(), name="signup"),
    path("logout/", views.log_out, name="logout"),
    path("<int:pk>/profile/", views.UserProfileView.as_view(), name="profile"),
]
