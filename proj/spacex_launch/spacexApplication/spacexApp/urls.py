from django.urls import include, re_path
from . import views

urlpatterns = [
    #Home page
    re_path(r'^$', views.index, name='index'),
    #re_path('', views.upcoming_launch, name='upcoming launch'),
]