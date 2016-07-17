from django.conf.urls import url
from mysite import views


urlpatterns = [
    url(r'^$', views.home, name='home-page'),
    url(r'^login/$', views.login, name='login-page'),
    url(r'^new/$', views.create_notes, name='new-note'),
    url(r'^scrum/$', views.scrum, name='scrum')
]