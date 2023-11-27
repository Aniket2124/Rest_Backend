from django.urls import path, include
from .views import postView, post_detail, PostDetailAPIView, PostAPIView, PostGenericApiView, PostViewset,PostViewsetMixin
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register('post',PostViewset, basename='post')
routers.register('postmixin',PostViewsetMixin, basename='postmixin')
urlpatterns = [
    path('posts/', postView, name='posts'),
    path('detail/<int:pk>', post_detail, name='detail'),
    path('posts_api/', PostAPIView.as_view(), name='posts'),
    path('detail_api/<int:pk>', PostDetailAPIView.as_view(), name='detail'),
    path('post_generic_api/<int:id>/', PostGenericApiView.as_view(), name='post_generic_api'),
    path('',include(routers.urls))
    
]
