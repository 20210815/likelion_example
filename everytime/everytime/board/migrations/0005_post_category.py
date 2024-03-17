# Generated by Django 5.0.3 on 2024-03-17 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_post_scrap_users_postlike_post_like_users'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='category.category'),
        ),
    ]
