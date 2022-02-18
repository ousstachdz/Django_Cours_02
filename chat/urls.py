from django.urls import path

from . import views

urlpatterns = [
    path('users', views.UserAPI.as_view(), name='chat_users_api'),
    path('users/<str:pk>', views.UserAPI.as_view(), name='chat_users_api'),
    path('messages', views.MessageAPI.as_view(), name='chat_messages_api'),
    path('messages/<str:pk>', views.MessageAPI.as_view(), name='chat_message_api'),
    path('comments', views.CommentAPI.as_view(), name='chat_comments_api'),
    path('comments/<str:pk>', views.CommentAPI.as_view(), name='chat_comment_api'),
    path('posts', views.PostAPI.as_view(), name='chat_posts_api'),
    path('posts/<str:pk>', views.PostAPI.as_view(), name='chat_post_api'),
]
