# Generated by Django 4.2.8 on 2024-01-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('position', models.CharField(max_length=100, verbose_name='должность')),
                ('phone', models.CharField(max_length=18, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
                'ordering': ('first_name', 'last_name', 'position', 'phone', 'email'),
            },
        ),
    ]
