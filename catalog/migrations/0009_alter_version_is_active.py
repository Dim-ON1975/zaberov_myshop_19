# Generated by Django 4.2.8 on 2024-02-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_version_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активная версия'),
        ),
    ]