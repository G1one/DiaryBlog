# Generated by Django 2.2.1 on 2019-05-21 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190521_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]