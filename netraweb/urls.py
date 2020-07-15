from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index,name="index"),
    path('',views.change_det,name='change_det'),
    path('fea_ext',views.fea_ext,name='fea_ext'),
    path('login',views.login,name='login'),
]