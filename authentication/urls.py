from django.conf.urls import url
from bookshop import views as core_views

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
]