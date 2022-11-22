from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewsSet, GroupViewsSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewsSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)
router.register('follow', FollowViewsSet, basename='Follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
