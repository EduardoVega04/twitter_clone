from django.contrib import admin
from .models import Post, Retweet, Like
from mptt.admin import MPTTModelAdmin


admin.site.register(Post, MPTTModelAdmin)
admin.site.register(Retweet)
admin.site.register(Like)
