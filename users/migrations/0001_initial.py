# Generated by Django 3.2.9 on 2022-01-26 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=180, null=True)),
                ('profile_pic', models.ImageField(default='default_profile_pic.jpg', upload_to=users.models.profile_pic_path, verbose_name='')),
                ('cover_pic', models.ImageField(default='default_header_pic.png', upload_to=users.models.cover_pic_path, verbose_name='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
