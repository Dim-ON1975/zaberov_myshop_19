from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from account.forms import UserRegisterForm, UserProfileForm
from account.models import User
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('account:update_profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(DetailView):
    model = User
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')

    def get_object(self, queryset=None):
        return self.request.user
