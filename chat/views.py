from unittest import result
from rest_framework.generics import GenericAPIView , mixins
from django.contrib.auth.models import User

from .serializers import MessageSerializer, CommentSerializer, PostSerializer, UserSerializer
from .models import Message, Comment, Post


class UserAPI(GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin, 
            mixins.UpdateModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get(self, request, pk=None):
        if (pk):
            return self.retrieve(request) 
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class PostAPI(GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin, 
            mixins.UpdateModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, pk=None):
        if (pk):
            return self.retrieve(request) 
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class MessageAPI(GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin, 
            mixins.UpdateModelMixin):
    # class meta:
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    
    def get(self, request, pk=None):
        if (pk):
            return self.retrieve(request) 
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class CommentAPI(GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin, 
            mixins.UpdateModelMixin):
    # class meta:
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    
    def get(self, request, pk=None):
        if (pk):
            return self.retrieve(request) 
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# Create your views here.
