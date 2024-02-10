# Generated by Django 4.2.8 on 2024-02-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_version_is_active_alter_version_name_version_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='name_version',
            field=models.CharField(choices=[('базовая', 'базовая'), ('новинка', 'новинка'), ('распродажа', 'распродажа'), ('скидка', 'скидка'), ('витрина', 'витрина'), ('уценённый', 'уценённый')], default='базовая', max_length=10, verbose_name='название'),
        ),
    ]