from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins,viewsets
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser,JSONParser
from .serializers import PostsSerializer,CommentsSerializer,LikesSerializer,CommentsSerializerPostUpdateDelete,LikesSerializerPostUpdateDelete
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
# from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser,JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class PostsViewSet(ModelViewSet):
    serializer_class=PostsSerializer
    queryset=Posts.objects.all()
    permission_classes=[IsAuthenticated]
    lookup_field='pk'

    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(author=user)
        return user



class CommentsViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class=CommentsSerializerPostUpdateDelete
    queryset=Comments.objects.all()
    permission_classes=[IsAuthenticated]
    lookup_field='pk'

    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(author=user)
        return user

class CommentViewSetListRetrieve(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)
    lookup_field='pk'





class LikesViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class=LikesSerializerPostUpdateDelete
    queryset=Likes.objects.all()
    permission_classes=[IsAuthenticated]
    lookup_field='pk'
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    def perform_create(self, serializer):
        postId = serializer.validated_data['postId']
        user = self.request.user

        if Likes.objects.filter(author=user, postId=postId).exists():
            like = Likes.objects.filter(author=user, postId=postId)
            like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer.save(author=self.request.user)

    def get_queryset(self):
        return Likes.objects.filter(author=self.request.user)

class LikesViewSetListRetrieve(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class=LikesSerializer
    queryset=Likes.objects.all()
    permission_classes=[IsAuthenticated]
    lookup_field='pk'
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)