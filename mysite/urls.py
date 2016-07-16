from django.conf.urls import url
from mysite import views


urlpatterns = [
    url(r'^$', views.home, name='home-page'),
    url(r'^login$', views.login, name='login-page')
]