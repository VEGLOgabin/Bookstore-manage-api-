from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from accounts.models import User,BookManagerUser,Profil,AdminUser
from rest_framework import viewsets,mixins
from djoser.views import UserViewSet
from rest_framework.views import APIView
from accounts.serializers import UserSerializer,BookManagerSerializer,ProfilSerializer,AdminUserSerializer,BookManagerSerializerList,ProfilSerializerList,AdminUserSerializerList,UserSerializerList
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser,JSONParser

# from rest_framework import viewsets, status
from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# All users here
class UserListViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=User.objects.all()
    serializer_class=UserSerializerList
    permission_classes=(IsAuthenticated,)





class SuperuserCreateViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,JSONParser)


    def perform_create(self, serializer):
        # Vérifier que l'utilisateur en cours est un super-utilisateur
        if not self.request.user.ISADMIN:
            return Response({'detail': 'Vous devez être un super-utilisateur pour effectuer cette opération.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer.save()

class SuperuserCreateViewSetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializerList
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,JSONParser)


class BookManagerViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=BookManagerSerializer
    queryset=BookManagerUser.objects.all()
    permission_classes=[IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):

        if not self.request.user.ISADMIN:
            return Response({'detail': 'Vous devez être un super-utilisateur pour effectuer cette opération.'}, status=status.HTTP_403_FORBIDDEN)

        else:
            AdminCreator=AdminUser.objects.get(user=self.request.user)
            serializer.save(AdminCreator=AdminCreator)

    
        

class BookManagerViewSetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=BookManagerSerializerList
    queryset=BookManagerUser.objects.all()
    permission_classes=[IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,JSONParser)




class ProfilViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=ProfilSerializer
    permission_classes=[IsAuthenticated]
    queryset=Profil.objects.all()
    parser_classes = (MultiPartParser, FormParser,JSONParser)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        # return user


class ProfilViewSetList(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ProfilSerializerList
    permission_classes=[IsAuthenticated]
    queryset=Profil.objects.all()
    parser_classes = (MultiPartParser, FormParser,JSONParser)




