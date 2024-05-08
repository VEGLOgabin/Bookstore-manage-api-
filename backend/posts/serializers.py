from rest_framework.serializers import ModelSerializer
from .models import Posts,Comments,Likes


class PostsSerializer(ModelSerializer):
    class Meta:
        model=Posts
        fields=['id','content','author','dateCreated','comments','likes']
        depth=1


class CommentsSerializer(ModelSerializer):
    class Meta:
        model=Comments
        fields=['id','content','postId','author','dateTimeCreated']
        depth=1

class CommentsSerializerPostUpdateDelete(ModelSerializer):
    class Meta:
        model=Comments
        fields=['id','content','postId','author','dateTimeCreated']
        # depth=1

class LikesSerializerPostUpdateDelete(ModelSerializer):
    class Meta:
        model=Likes
        fields=['id','postId','author']
        # depth=1


class LikesSerializer(ModelSerializer):
    class Meta:
        model=Likes
        fields=['id','postId','author']
        depth=1

