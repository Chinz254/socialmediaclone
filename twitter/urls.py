from django.urls import path

from . import views


urlpatterns = [
    path('likes/', views.tweet_lyk, name='tweet_lyk'),
    path('', views.account, name='account'),
    path('signout/', views.signout, name='signout'),
]