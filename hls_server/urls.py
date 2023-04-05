from django.contrib import admin
from django.urls import path, include
from hls_server import views
    
urlpatterns = [
    path('hls/<str:cam_num>/', views.hls_view, name='hls'),
    path('hls/<str:cam_num>/<str:filename>', views.hls_view, name='hls')
]
