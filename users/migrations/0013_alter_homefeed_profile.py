# Generated by Django 3.2.9 on 2022-01-31 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_feed_homefeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homefeed',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed', to='users.profile'),
        ),
    ]
