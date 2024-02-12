from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views import View

from account.forms import UserRegisterForm, UserProfileForm, AuthenticationForm
from account.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from account.services import send_email_for_verify
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class MyLoginView(LoginView):
    """Авторизация"""
    form_class = AuthenticationForm
    template_name = "account/login.html"


class RegisterView(CreateView):
    """Регистрация"""
    model = User
    form_class = UserRegisterForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )
        send_email_for_verify(self.request, user)
        return redirect('account:confirm_email')


class EmailVerify(View):
    """Верификация почты при регистрации"""

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('account:login')
        return redirect('account:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() декодирует в байт-строку
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


class ProfileUpdateView(UpdateView):
    """Редактирование профиля"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('account:update_profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(DetailView):
    """Просмотр профиля"""
    model = User
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(DeleteView):
    """Удаление пользователя"""
    model = User
    success_url = reverse_lazy('account:login')

    def get_object(self, queryset=None):
        return self.request.user


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
    template_name = "account/password_change_form.html"


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "account/password_change_done.html"


class MyPasswordResetView(PasswordResetView):
    email_template_name = "account/password_reset_email.html"
    success_url = reverse_lazy("account:password_reset_done")
    template_name = "account/password_reset_form.html"


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("account:password_reset_complete")
    template_name = "account/password_reset_confirm.html"


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "account/password_reset_complete.html"

