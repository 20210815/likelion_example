# Generated by Django 5.0.3 on 2024-03-15 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0002_alter_post_anonymity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='board.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
