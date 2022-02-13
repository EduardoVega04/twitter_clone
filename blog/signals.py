from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post, Like, Retweet

# Theory here: https://www.youtube.com/watch?v=rEX50LJrFuU
# Don't forget to register the signals in apps.py

@receiver(post_save, sender=Post)
def fan_out_post(sender, **kwargs):
    """Signal triggered after a new post is created.
    Sends the new post to the home feed of all followers"""
    instance = kwargs['instance']
    post_author = instance.author
    if kwargs.get('created') is not None:
        for follower in post_author.followers.all():
            follower.homefeed.following_tweets.add(instance)


@receiver([post_save, post_delete], sender=Like)
def fan_out_like(sender, **kwargs):
    """Signal triggered after a new like is created.
    Sends/deletes the new like to/from the home feed of all followers
    Sends/deletes the new like to/from the profile feed of the like author"""
    instance = kwargs['instance']
    like_author = instance.author
    if kwargs.get('created') is not None:
        like_author.profilefeed.liked.add(instance.related_post)
        for follower in like_author.followers.all():
            follower.homefeed.following_likes.add(instance.related_post)
    else:
        like_author.profilefeed.liked.remove(instance.related_post)
        for follower in like_author.followers.all():
            follower.homefeed.following_likes.remove(instance.related_post)


@receiver([post_save, post_delete], sender=Retweet)
def fan_out_retweet(sender, **kwargs):
    """Signal triggered after a new retweet is created.
    Sends/deletes the new retweet to/from the home feed of all followers
    Sends/deletes the new retweet to/from the profile feed of the retweet author"""
    instance = kwargs['instance']
    retweet_author = instance.author
    if kwargs.get('created') is not None:
        retweet_author.profilefeed.retweeted.add(instance.related_post)
        for follower in retweet_author.followers.all():
            follower.homefeed.following_retweets.add(instance.related_post)
    else:
        retweet_author.profilefeed.retweeted.remove(instance.related_post)
        for follower in retweet_author.followers.all():
            follower.homefeed.following_retweets.remove(instance.related_post)
