from django.conf.urls import url
from maiziapp.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^login', do_login, name='login'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^course/$',course,name='course'),
    url(r'^course_play/(?P<courseid>\w+)/$', course_play, name='course_play'),
    url(r'^course_play/lesson/(?P<courseid>\w+)/(?P<lessonid>\w+)/$', course_play, name='course_play'),
    url(r'^discuss_post/$', discuss_post, name='discuss_post'),
    url(r'^teacher/(?P<teacherid>\w+)$',teacher,name='teacher'),
    url(r'^student/(?P<studentid>\w+)$',student,name='student'),
    url(r'^change', do_change, name='change'),
]

