from django.contrib import admin
from .models import Post
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Post, MPTTModelAdmin)
