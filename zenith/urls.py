from django.urls import path

from . import views, api_views, proxy_views

urlpatterns = [
    path('api/proxy/get', proxy_views.Get.as_view()),
    path('api/proxy/post', proxy_views.Post.as_view()),
    
    path('api/login', api_views.Login.as_view()),
    path('api/list', api_views.List.as_view()),
    path('api/status/<str:type>/<str:code>', api_views.Status.as_view()),
]
