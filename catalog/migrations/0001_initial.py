# Generated by Django 4.2.8 on 2024-01-13 10:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='наименование')),
                ('description', models.TextField(max_length=1000, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='наименование')),
                ('description', models.TextField(max_length=1000, verbose_name='описание')),
                ('img', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='превью')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('date_change', models.DateField(auto_now=True, verbose_name='дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name', 'category', 'price', 'date_creation', 'date_change'),
            },
        ),
    ]
