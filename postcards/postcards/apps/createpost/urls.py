from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('acc', views.acc, name='acc'),
    #path('registration', views.registration, name='registration'),
    #path('account', include('django.contrib.auth.urls')),

    #path('test', views.test, name='test_what')
]