from django.conf.urls import urls
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^login/$', auth_views.login name='login'),
    url(r'^registration/$', views.reg_form, name='registration_form'),
    url(r'^article/$', views.publish_article, name='publish_article'),
    url(r'^question/$', views.ask_question, name='ask_question'),
    url(r'^answer/$', views.answer_question, name='answer_question'),
    url(r'^comment/$', views.comment, name='comment'),
]

