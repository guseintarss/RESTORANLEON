from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu', views.menu),
    path('blog', views.blog),
    path('otzv', views.otvz),
    path('bakets', views.bakets),
    path('inter', views.inter),
    path('korp', views.korp),
]
