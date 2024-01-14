# Generated by Django 4.2.8 on 2024-01-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name', 'category', 'price', 'date_add', 'date_update'), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_creation',
            new_name='date_add',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_change',
            new_name='date_update',
        ),
    ]