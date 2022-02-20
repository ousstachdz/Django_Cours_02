from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message, Comment, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        # instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        # instance.owner = validated_data.get('owner', instance.owner)
        # instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        # instance.owner = validated_data.get('owner', instance.owner)
        instance.post = validated_data.get('post', instance.post)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, queryset = Post.objects.all())
    # messages = serializers.PrimaryKeyRelatedField(many = True, queryset = Message.objects.all())
    # comments = serializers.PrimaryKeyRelatedField(many = True, queryset = Comment.objects.all())
    owner = serializers.ReadOnlyField(source = 'owner.username')
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'messages', 'comments', 'owner']
        # fields = ['id', 'username','owner', 'posts']