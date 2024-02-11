from django.urls import path
from account.apps import AccountConfig
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from account.views import RegisterView, ProfileUpdateView, ProfileDetailView, UserDeleteView, EmailVerify, MyLoginView


app_name = AccountConfig.name

urlpatterns = [
    # Авторизация
    path('', MyLoginView.as_view(), name='login'),
    # Выход
    path('logout/', LogoutView.as_view(), name='logout'),
    # Регистрация
    path('register/', RegisterView.as_view(), name='register'),
    # Сообщение об отправке на почту подтверждения
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    # Подтверждение email
    path('confirm_email/', TemplateView.as_view(template_name='account/confirm_email.html'), name='confirm_email'),
    # Некорректный токен
    path('invalid_verify/', TemplateView.as_view(template_name='account/invalid_verify.html'), name='invalid_verify'),
    # Редактирование профиля
    path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
    # Просмотр профиля
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    # Удаление профиля
    path('delete_profile/', UserDeleteView.as_view(), name='user_delete'),

]
