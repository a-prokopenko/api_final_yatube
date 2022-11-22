from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewsSet, GroupViewsSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewsSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('follow', FollowViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]
