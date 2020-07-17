from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index,name="index"),
    path('',views.change_det,name='change_det'),
    path('change_detection',views.change_detection,name='change_detection'),
    path('change_detected_result',views.change_detected_result,name='change_detected_result'),
    path('feature_extraction',views.feature_extraction,name='feature_extraction'),
    path('fea_ext',views.fea_ext,name='fea_ext'),
    path('login',views.login,name='login'),
    path('loader',views.loader,name='loader'),
    path('new_login',views.new_login,name='new_login'),
]