from django.urls import path, include

from . import views

urlpatterns = [
    path('signup', views.account, name='account'),
    path('', views.account_login, name='account'),
   # path('account', include('django.contrib.auth.urls')),

    #path('test', views.test, name='test_what')
]