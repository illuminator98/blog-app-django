from django.urls import path
from . import views

urlpatterns = [
    # path('posts', views.PostViewSet.as_view({
    #     'get': 'get_all_posts',
    #     'post': 'create_post'
    # }), name='post_list'),
    path('posts/<int:posts_id>',views.PostViewSet.as_view({
        'get':'get_post',
        'delete':'delete_post',
        'patch' :'edit_post'
    }),name='post_detail'),
    path('posts/all',views.get_all_posts,name='post_list'),
    path('create/post',views.create_post,name='create_post'),
    path('posts/<int:post_id>/comment',views.create_comment,name='create_comment'),
    path('posts/<int:post_id>/comment/<int:comment_id>',views.CommentViewSet.as_view({
        'delete':'delete_comment',
        'patch':'edit_comment'
    }),name='get_comment'),
    path('<int:user_id>/posts',views.get_all_user_posts,name='all_user_posts'),
    path('username/',views.get_username,name='get_username'),
    path('age/',views.get_age, name='get_age')
]
# 