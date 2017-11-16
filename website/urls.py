from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dish/(?P<pk>\d+)/$', views.dish_detail, name='dish_detail'),
]
