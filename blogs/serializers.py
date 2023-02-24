
from rest_framework import serializers
from .models import Post,Comment
from login.serializers import UserSerializer,UserProfileSerializer


class CommentSerializer(serializers.ModelSerializer):   
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['user','text','post','id']

class CreateCommentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    
    

    class Meta:
        model = Post
        fields = ['id','title','text','user','comment_set']
    
    
    