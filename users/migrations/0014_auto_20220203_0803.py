# Generated by Django 3.2.9 on 2022-02-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_author'),
        ('users', '0013_alter_homefeed_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homefeed',
            name='following_likes',
        ),
        migrations.RemoveField(
            model_name='homefeed',
            name='following_retweets',
        ),
        migrations.RemoveField(
            model_name='homefeed',
            name='following_tweets',
        ),
        migrations.AddField(
            model_name='homefeed',
            name='my_likes',
            field=models.ManyToManyField(blank=True, related_name='home_feeds_like', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='homefeed',
            name='my_retweets',
            field=models.ManyToManyField(blank=True, related_name='home_feeds_retweet', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='homefeed',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homefeed', to='users.profile'),
        ),
        migrations.CreateModel(
            name='ProfileFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_likes', models.ManyToManyField(blank=True, related_name='profile_feeds_like', to='blog.Post')),
                ('following_retweets', models.ManyToManyField(blank=True, related_name='profile_feeds_retweet', to='blog.Post')),
                ('following_tweets', models.ManyToManyField(blank=True, related_name='profile_feeds_tweet', to='blog.Post')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profilefeed', to='users.profile')),
            ],
        ),
    ]
