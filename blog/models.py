from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from .validators import validate_file_type
import os
from mptt.models import MPTTModel, TreeForeignKey


def post_media_path(instance, filename):
    return os.path.join(str(instance.author.pk), 'tweets_media', filename)


# https://www.youtube.com/watch?v=8jWr3ewz2S4
class Post(MPTTModel):
    content = models.CharField(max_length=180, verbose_name="", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    media = models.FileField(
        verbose_name="", blank=True, null=True, upload_to=post_media_path, validators=[validate_file_type])
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['date_posted']

# https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.full_clean
# https://djangocentral.com/custom-model-validation-in-django/

    def clean(self):
        if not self.content and not self.media:
            raise ValidationError("Post must contain any content!")

    def save(self, *args, **kwargs):    
        self.full_clean()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        if self.content:
            return self.content[:15]
        else:
            return "Default title"


class Retweet(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
