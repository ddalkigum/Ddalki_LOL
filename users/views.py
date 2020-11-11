import requests
import os
from django.views.generic import DetailView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse, redirect
from users import models, forms, mixins


class UserLoginView(FormView):

    form_class = forms.UserLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class UserProfileView(mixins.LoginOnlyView, DetailView):

    model = models.User
    template_name = "users/profile.html"
    context_object_name = "user_obj"


class UserSignupView(FormView):

    form_class = forms.UserSignupForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def kakao_login(request):
    client_id = os.environ.get("KAKAO_KEY")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    code = request.GET.get("code")
    client_id = os.environ.get("KAKAO_KEY")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
    )
    token_json = token_request.json()
    if token_json is None:
        raise Exception("Can't do it")
    access_token = token_json.get("access_token")
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()
    kakao_account = profile_json.get("kakao_account")
    kakao_profile = kakao_account.get("profile")
    kakao_nickname = kakao_profile.get("nickname")
    kakao_email = kakao_account.get("email")
    kakao_id = profile_json.get("id")

    if models.User.objects.exists():
        user = models.User.objects.get(email=kakao_email)
    else:
        user = models.User.objects.create(
            username=kakao_email,
            email=kakao_email,
            nickname=kakao_nickname,
        )
        user.save()

    login(request, user)
    return redirect(reverse("core:home"))
