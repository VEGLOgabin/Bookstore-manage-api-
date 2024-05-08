from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from posts.views import PostsViewSet,CommentsViewSet,LikesViewSet,CommentViewSetListRetrieve,LikesViewSetListRetrieve

router=DefaultRouter()

router.register('posts', PostsViewSet,basename='post')
router.register('comments', CommentsViewSet)
router.register('comment', CommentViewSetListRetrieve)
router.register('likes',LikesViewSet,basename='likeCreate')
router.register('like',LikesViewSetListRetrieve,basename='likeList')





urlpatterns=[
    path('', include(router.urls)),
]