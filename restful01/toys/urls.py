from django.conf.urls import url
from toys import views

# Create your URL patterns.

urlpatterns = [
    url(r'^toys/$', views.toy_list),
    url(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),
]
