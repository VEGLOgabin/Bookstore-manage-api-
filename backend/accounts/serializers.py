from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import serializers
from .models import Profil,BookManagerUser,AdminUser


User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','first_name','last_name','password','email','is_active','ISADMIN','is_manager','ProfilPhoto')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}
        #depth = 1

class UserSerializerList(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','first_name','last_name','password','email','is_active','ISADMIN','is_manager','ProfilPhoto')
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}
        depth = 1



class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminUser
        fields=['id','user','level','profession']

class AdminUserSerializerList(serializers.ModelSerializer):
    class Meta:
        model=AdminUser
        fields=['id','user','level','profession']
        depth=1




class BookManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookManagerUser
        fields=['id','user','AdminCreator','degree','experienceYears']

class BookManagerSerializerList(serializers.ModelSerializer):
    class Meta:
        model=BookManagerUser
        fields=['id','user','AdminCreator','degree','experienceYears']
        depth=1
        


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields=['id','user','image']
    
        


class ProfilSerializerList(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields=['id','user','image']
        depth=1




