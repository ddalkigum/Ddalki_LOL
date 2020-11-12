from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Tip
from users import mixins
from champions import models as champion_model
from users import models as user_model


@login_required(login_url="users:login")
def create_tips(request, pk):
    if request.method == "GET":
        user = request.user

        champion = champion_model.Champion.objects.get(pk=pk)
        form = forms.TipCreateForm
        return render(
            request,
            template_name="champions/tips.html",
            context={
                "champion": champion,
                "form": form,
                "user": user,
            },
        )

    if request.method == "POST":
        form = forms.TipCreateForm
        if form.is_valid:
            champion = champion_model.Champion.objects.get(pk=pk)
            user_pk = request.user.pk
            user = user_model.User.objects.get(pk=user_pk)
            description = request.POST.get("description")
            Tip.objects.create(
                user=user,
                champion=champion,
                description=description,
            )

            return redirect(reverse("champions:detail", kwargs={"pk": pk}))


@login_required(login_url="users:login")
def delete_tips(request, pk):
    if request.method == "GET":
        return render(request, "mixins/auth/delete.html")

    if request.method == "POST":
        tip = Tip.objects.get(pk=pk)
        tip.delete()
        return redirect(
            reverse("champions:champion"),
        )
