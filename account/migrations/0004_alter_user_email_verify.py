# Generated by Django 4.2.8 on 2024-02-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False, verbose_name='верификация почты'),
        ),
    ]
