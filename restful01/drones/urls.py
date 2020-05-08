from django.conf.urls import url
from drones import views

urlpatterns = [
    url('^drone-categories/$', views.DroneCategoryList.as_view(),
        name=views.DroneCategoryList.name),
    url('^drone-categories/(?P<pk>[0-9])/$', views.DroneCategoryDetail.as_view(
    ), name=views.DroneCategoryDetail.name),
    url('^drones/$', views.DroneList.as_view(), name=views.DroneList.name),
    url('^drones/(?P<pk>[0-9])/$', views.DroneDetail.as_view(),
        name=views.DroneDetail.name),
    url('^pilots/$', views.PilotList.as_view(), name=views.PilotList.name),
    url('^pilots/(?P<pk>[0-9])/$', views.PilotDetail.as_view(),
        name=views.PilotDetail.name),
    url('^competitions/$', views.CompetitionList.as_view(),
        name=views.CompetitionList.name),
    url('^competitions/(?P<pk>[0-9])/$', views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
