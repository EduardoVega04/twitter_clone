from django.urls import path
from .views import home, about

app_name = "blog"
urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about"),
]
