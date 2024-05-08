from django.shortcuts import render
from .models import *
from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import BooksSerializerPost,CategorySerializer,CommandBookSerializer,ValidateCommandSerializer,BooksSerializerList,HistorySerializer,HistorySerializerList,CategorySerializerList,CommandBookSerializerList,ValidateCommandSerializerList
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser,FileUploadParser



class BooksViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=BooksSerializerPost
    queryset=Books.objects.all()
    permission_classes=[IsAuthenticated]
    parser_classes=(MultiPartParser,FormParser,FileUploadParser,JSONParser)


    def perform_create(self, serializer):
        addBy=BookManagerUser.objects.get(user=self.request.user)
        serializer.save(addBy=addBy)
        return serializer


class BooksViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=BooksSerializerList
    queryset=Books.objects.all()
    permission_classes=[IsAuthenticated]
    parser_classes=(MultiPartParser,FormParser,FileUploadParser,JSONParser)




class CategoryViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,JSONParser)
    def perform_create(self, serializer):
        create_By=BookManagerUser.objects.get(user=self.request.user)
        serializer.save(create_By=create_By)
        


class CategoryViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=CategorySerializerList
    queryset=Category.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)



class CommandBookViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=CommandBookSerializer
    queryset=CommandBooks.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
        


class CommandBookViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=CommandBookSerializerList
    queryset=CommandBooks.objects.all()
    permission_classes=[IsAuthenticated]
    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)



class ValidateCommandViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ValidateCommandSerializer
    queryset=ValidateCommands.objects.all()
    permission_classes=[IsAuthenticated]

    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)

    def perform_create(self, serializer):
        validator=BookManagerUser.objects.get(user=self.request.user)
        serializer.save(validator=validator)
        



class ValidateCommandViewSetList(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=ValidateCommandSerializerList
    queryset=ValidateCommands.objects.all()
    permission_classes=[IsAuthenticated]

    # parser_classes = (MultiPartParser, FormParser,FileUploadParser,JSONParser)



class HistoryViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=HistorySerializer
    queryset=History.objects.all()
    # parser_classes=(MultiPartParser, FormParser,FileUploadParser,JSONParser)
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        validated_by=BookManagerUser.objects.get(user=self.request.user)
        serializer.save(validated_by=validated_by)




class HistoryViewSetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=HistorySerializerList
    queryset=History.objects.all()
    # parser_classes=(MultiPartParser, FormParser,FileUploadParser,JSONParser)
    permission_classes=[IsAuthenticated]



