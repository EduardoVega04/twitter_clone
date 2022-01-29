# Generated by Django 3.2.9 on 2022-01-29 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('users', '0004_alter_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pinned_tweet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
