from django.conf.urls import url
from . import views

urlpatterns = [

    url(
        r'^v1/search/$',
        views.ScoreAPI.as_view(),
        name='Score API'
    ),

    url(
        r'^v1/data/$',
        views.DataProcessingAPI.as_view(),
        name='Data Processing'
    ),
    ]