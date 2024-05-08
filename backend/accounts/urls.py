from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from accounts.views import BookManagerViewSet,ProfilViewSet,SuperuserCreateViewSet,BookManagerViewSetList,ProfilViewSetList,SuperuserCreateViewSetList,UserListViewSet

router=DefaultRouter()

# router.register('auth', AccountUserViewset,basename='auth')
router.register('booksmanagers', BookManagerViewSet,basename='books-managers')
router.register('booksmanagerslist', BookManagerViewSetList,basename='booksmanagers')
router.register('imgprofil',ProfilViewSet,basename='image-profil')
router.register('imgprofillist',ProfilViewSetList,basename='imageprofil')
router.register('superuser', SuperuserCreateViewSet, basename='superuser')
router.register('superuserlist', SuperuserCreateViewSetList, basename='superuserAdmin')
router.register('user', UserListViewSet,basename='Users')




urlpatterns=[
    path('', include(router.urls)),
    # path('user/',UserListViewSet.as_view({'get': 'list'}),name='Users'),
]