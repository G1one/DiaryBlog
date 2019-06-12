# Generated by Django 2.2.1 on 2019-05-23 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_profile_users_reaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commets_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_slug', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('moderation', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_for_commets', to=settings.AUTH_USER_MODEL, verbose_name='аккаунт пользователя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_commets', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
