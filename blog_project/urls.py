"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# It is a good practice to always version your APIs—v1/, v2/, etc—
# since when you make a large change there may be some lag time 
# before various consumers of the API can also update


# Going forward whenever we want to switch between user accounts we’ll need to jump
# into the Django admin, log out of one account and log in to another. Each and every
# time. Then switch back to our API endpoint.