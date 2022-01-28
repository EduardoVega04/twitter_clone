"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('<str:username>/', include('users.urls')),
    # By default, django looks at registration/login.html, but that can be customized in the parameter
    # After successful login, it redirects to accounts/profile. Set LOGIN_REDIRECT_URL in settings.py
    # Remember that login/ and logout/ are not part of any aplication
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Not specifying a custom logout template will cause Django to use the default admin logout page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]

# Serves the /media/ static files
# ONLY for development mode, DO NOT use in production!
# That's why the DEBUG variable in settings is checked
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
