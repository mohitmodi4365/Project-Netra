from django.urls import path
from . import views
from netra import settings
from django.conf.urls.static import static
urlpatterns = [
    path("index",views.index,name="index"),
    path('change_det',views.change_det,name='change_det'),
    path('change_detection',views.change_detection,name='change_detection'),
    path('change_detection_result',views.change_detection_result,name='change_detection_result'),
    path('feature_extraction',views.feature_extraction,name='feature_extraction'),
    path('fea_ext',views.fea_ext,name='fea_ext'),
    path('login',views.login,name='login'),
    path('loader',views.loader,name='loader'),
    path('',views.new_login,name='new_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)