from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_listURL'),
    url(r'^post/(?P<pk>\d+)/$',
        views.post_detail, name='post_detailURL'),
]
