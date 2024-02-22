from django.urls import path, include
from account.apps import AccountConfig
from django.contrib.auth.views import LogoutView, TemplateView, PasswordResetConfirmView, PasswordResetCompleteView
from account.views import RegisterView, ProfileUpdateView, ProfileDetailView, UserDeleteView, EmailVerify, MyLoginView, \
    MyPasswordChangeDoneView, MyPasswordChangeView, MyPasswordResetView, MyPasswordResetDoneView, \
    MyPasswordResetConfirmView, MyPasswordResetCompleteView
from django.views.decorators.cache import never_cache

app_name = AccountConfig.name

urlpatterns = [
    # Авторизация
    path('login/', never_cache(MyLoginView.as_view()), name='login'),
    # Выход
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    # Смена пароля
    path('password-change/', never_cache(MyPasswordChangeView.as_view()), name='password_change'),
    path('password-change/done/', never_cache(MyPasswordChangeDoneView.as_view()), name='password_change_done'),
    # Сброс пароля
    path('password-reset/', never_cache(MyPasswordResetView.as_view()), name='password_reset'),
    path('password-reset/done/', never_cache(MyPasswordResetDoneView.as_view()), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', never_cache(MyPasswordResetConfirmView.as_view()),
         name='password_reset_confirm'),
    path('password-reset/complete/', never_cache(MyPasswordResetCompleteView.as_view()),
         name='password_reset_complete'),
    # Регистрация
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    # Сообщение об отправке на почту подтверждения
    path('verify_email/<uidb64>/<token>/', never_cache(EmailVerify.as_view()), name='verify_email'),
    # Подтверждение email
    path('confirm_email/', never_cache(TemplateView.as_view(template_name='account/confirm_email.html')),
         name='confirm_email'),
    # Некорректный токен
    path('invalid_verify/', never_cache(TemplateView.as_view(template_name='account/invalid_verify.html')),
         name='invalid_verify'),
    # Редактирование профиля
    path('update_profile/', never_cache(ProfileUpdateView.as_view()), name='update_profile'),
    # Просмотр профиля
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    # Удаление профиля
    path('delete_profile/', never_cache(UserDeleteView.as_view()), name='user_delete'),
]
