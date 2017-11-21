from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dish/(?P<pk>\d+)/$', views.dish_detail, name='dish_detail'),
    url(r'^restaurant/(?P<pk>\d+)/$', views.restaurant_detail, name='restaurant_detail'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
