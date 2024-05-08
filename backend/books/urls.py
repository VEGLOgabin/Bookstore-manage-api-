from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from books.views import BooksViewSet,CategoryViewSet,CommandBookViewSet,ValidateCommandViewSet,BooksViewSetList,CategoryViewSetList,CommandBookViewSetList,ValidateCommandViewSetList,HistoryViewSet,HistoryViewSetList

router=DefaultRouter()

router.register('books', BooksViewSet,basename='books')
router.register('category', CategoryViewSet,basename='book-category')
router.register('commandbook',CommandBookViewSet,basename='command-book')
router.register('validatebookcommand',ValidateCommandViewSet,basename='validate-book-command')

router.register('bookslist', BooksViewSetList,basename='books-list')
router.register('categorylist', CategoryViewSetList,basename='book-category-list')
router.register('commandbooklist',CommandBookViewSetList,basename='command-book-list')
router.register('validatebookcommandlist',ValidateCommandViewSetList,basename='validate-book-command-list')
router.register("history", HistoryViewSet,basename="history")
router.register("historylist", HistoryViewSetList,basename="historylist")



urlpatterns=[
    path('', include(router.urls)),
   

]