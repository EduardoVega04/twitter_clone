from django.urls import path
from . import views as user_views
from blog import views as blog_views

app_name = 'users'
urlpatterns = [
    path('', user_views.profile, name='profile'),
    path('update/', user_views.profileUpdate, name='profile-update'),
    path('status/<int:post_id>/', blog_views.post_detail, name='post-detail')
]
