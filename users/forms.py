from django import forms
from users import models


class UserLoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"}), label="이메일"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        max_length=20,
        label="비밀번호",
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 잘못됬습니다."))
        except models.User.DoesNotExist:
            self.errors.clear
            self.add_error("email", forms.ValidationError("유저가 존재하지않습니다."))


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("last_name", "email", "password", "password1")

    last_name = forms.CharField(widget=forms.TextInput, label="이름")
    email = forms.CharField(widget=forms.EmailInput, label="이메일")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("패스워드가 일치하지 않습니다.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
