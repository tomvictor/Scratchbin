from django.conf.urls import url
from mysite import views

urlpatterns = [
    url(r'^$', views.home, name='home-page'),
    url(r'^login/$', views.login, name='login-page'),
    url(r'^signup/$', views.sign_up, name='sign-up'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^new/$', views.create_notes, name='new-note'),
    url(r'^scrum/$', views.scrum, name='scrum'),
    url(r'^about/$', views.about, name='about-page'),
    url(r'^notes/(?P<id>\d+)/$', views.note_detail, name='detail'),
    url(r'^notes/(?P<id>\d+)/edit/$', views.update_notes, name='update'),
    url(r'^notes/(?P<id>\d+)/delete/$', views.delete_notes, name='delete')

]
