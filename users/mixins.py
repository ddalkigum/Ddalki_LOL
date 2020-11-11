from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class LoggoutOnlyView(LoginRequiredMixin):

    pass


class LoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "로그인이 필요합니다.")
        return redirect("users:login")