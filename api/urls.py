from django.urls import path
from . import views as api_views

app_name = 'api'
urlpatterns = [
    path('post/', api_views.post, name='post'),
    path('<int:post_id>/retweet/', api_views.retweet_post, name='retweet-post'),
    path('<int:post_id>/like/', api_views.like_post, name='like-post'),
    path('<int:post_id>/comment/', api_views.comment_post, name='comment-post'),
    path('<int:post_id>/delete/', api_views.delete_post, name='delete-post'),
    path('<int:post_id>/pin/', api_views.pin_post, name='pin-post'),
    path('<int:followee_id>/follow/', api_views.follow_user, name='follow-user'),
]
