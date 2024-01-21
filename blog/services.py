from django.core.mail import send_mail
from dotenv import load_dotenv, find_dotenv
import os
from core import settings

# переменные окружения в файле .env
load_dotenv(find_dotenv())


def sending_mail(title: str):
    """ Отправка письма по электронной почте """
    send_mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        subject='Ура! Сотый просмотр Вашего поста!',
        message=f'Поздравляем! Ваш пост "{title}" набирает популярность! Его посмотрели 100 раз!',
        recipient_list=[os.getenv('RECIPIENT_ONE'), os.getenv('RECIPIENT_TWO')],
        fail_silently=False,
    )
