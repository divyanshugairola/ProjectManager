from django.urls import path,include
from app1 import views

urlpatterns = [
path('',views.index,name="index"),
# url( r'^account/(?P<pk>\d+)/$', views.dashboard,name="dashboard"),
]
