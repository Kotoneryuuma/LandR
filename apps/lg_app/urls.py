from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.regi),
    url(r'^process/login$', views.login),
    url(r'^success$', views.success),
    url(r'^destroy$', views.destroy),
]
