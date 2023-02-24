from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,CreateCommentSerializer 
from rest_framework.viewsets import GenericViewSet
from login.serializers import UserSerializer
from .models import UserProfile
from login.serializers import UserProfileSerializer

@api_view(['GET'])
def get_username(request):
    user=User.objects.get(pk=request.user.id)
    serializer=UserSerializer(user)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.filter(user=request.user.userprofile)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=200)

# Create your views here.
class PostViewSet(GenericViewSet):
    def get_post(self,request,posts_id):
        post=get_object_or_404(Post, pk=posts_id)
        serializer=PostSerializer(post)
        return Response(serializer.data,status=200)


    def edit_post(self,request,posts_id):
        post=get_object_or_404(Post, pk=posts_id)
        request.data['user'] = request.user.id  
        if post.user.id != request.user.id:
            return Response(status=403)

        serializer=PostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors,status=400)


    def delete_post(self,request,posts_id):
        post=get_object_or_404(Post, pk=posts_id)
        if post.user.id != request.user.id:
            return Response(status=403)
        post.delete()
        return Response(status=204)


class CommentViewSet(GenericViewSet):
    def edit_comment(self,request,comment_id, post_id):
        request.data['post']=post_id
        comment=get_object_or_404(Comment, pk=comment_id)
        request.data['user'] = request.user.id  
        if comment.user.id != request.user.id:
            return Response(status=403)

        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors,status=400)


    def delete_comment(self,request,post_id, comment_id):
        request.data['post']=post_id
        comment=get_object_or_404(Comment, pk=comment_id)
        if comment.post.user.user.id == request.user.id or comment.user.user.id == request.user.id:
            comment.delete()
            return Response(status=204)
        return Response(status=403)


@api_view(['POST'])
def create_post(request):
    request.data['user'] = request.user.id
    serializer = PostSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data, status=201)    

@api_view(['POST'])
def create_comment(request, post_id):
    request.data['user'] = request.user.userprofile.id
    request.data['post'] = post_id
    serializer = CreateCommentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['GET'])
def  get_all_user_posts(request,username):
        get_object_or_404(User, username=username)
        posts = Post.objects.filter(user__user__username=username)
        user_serializer = UserSerializer(User.objects.get(username=username))
        serializer = PostSerializer(posts,many=True)
        return Response({'user': user_serializer.data, 'posts': serializer.data},status=200)
