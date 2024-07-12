from django.conf.urls import url

from oidc_auth import views

urlpatterns = [
    url(r'^login/$', views.login_begin, name='oidc-login'),
    url(r'^complete/$', views.login_complete, name='oidc-complete'),
]
