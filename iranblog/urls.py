"""iranblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from weblog.views import get_all_posts, get_single_post, author_profile,main_page,get_about,get_contact

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', main_page),
    path('posts/', get_all_posts),
    path('posts/<post_id>/', get_single_post),
    path('authors/<username>/', author_profile),
    path('about', get_about),
    path('contact', get_contact),

]
