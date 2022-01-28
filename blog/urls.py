from django.urls import path
from .views import home, about, follow_user

app_name = "blog"
urlpatterns = [
    path('', home, name="blog-home"),
    path('<str:followee>/follow/', follow_user, name='follow-user'),
    path('about/', about, name="blog-about"),
]
