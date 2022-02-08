from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from PIL import Image
import os


# https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.FileField.upload_to
def profile_pic_path(instance, filename):
    return os.path.join(str(instance.user.pk), 'profile_pics', 'profile_pic.png')


def cover_pic_path(instance, filename):
    return os.path.join(str(instance.user.pk), 'cover_pics', 'cover_pic.png')


def resize_image(img, width):
    wpercent = (width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    return img.resize((width, hsize), Image.ANTIALIAS)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=180, null=True, blank=True)
    profile_pic = models.ImageField(verbose_name="", default="default_profile_pic.jpg", upload_to=profile_pic_path)
    cover_pic = models.ImageField(verbose_name="", default="default_header_pic.png", upload_to=cover_pic_path)
    following = models.ManyToManyField('Profile', related_name='followers', blank=True)


    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    # Override the super save() method. Save image and then resize and save it again
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        profile_img = Image.open(self.profile_pic.path)
        cover_img = Image.open(self.cover_pic.path)

        if profile_img.height > 500 or profile_img.width > 500:
            resized_profile_img = resize_image(profile_img, 500)
            resized_profile_img.save(self.profile_pic.path)

        if cover_img.height > 1080 or cover_img.width > 1920:
            resized_cover_img = resize_image(cover_img, 1920)
            resized_cover_img.save(self.cover_pic.path)


class HomeFeed(models.Model):
    profile = models.OneToOneField(Profile, null=True, blank=True, on_delete=models.CASCADE, related_name='homefeed')
    following_tweets = models.ManyToManyField(Post, blank=True, related_name='profile_feeds_tweet')
    following_retweets = models.ManyToManyField(Post, blank=True, related_name='profile_feeds_retweet')
    following_likes = models.ManyToManyField(Post, blank=True, related_name='profile_feeds_like')


class ProfileFeed(models.Model):
    profile = models.OneToOneField(Profile, null=True, blank=True, on_delete=models.CASCADE, related_name='profilefeed')
    my_retweets = models.ManyToManyField(Post, blank=True, related_name='home_feeds_retweet')
    my_likes = models.ManyToManyField(Post, blank=True, related_name='home_feeds_like')
    pinned_tweet = models.OneToOneField(Post, blank=True, null=True, on_delete=models.CASCADE)
