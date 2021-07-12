#rest_framework
from rest_framework import mixins,viewsets
from rest_framework.response import Response
#permissions
from rest_framework.permissions import IsAuthenticated
from posts.permissions import IsAuthor

#models
from posts.models import Post, Author
#serializers
from posts.serializers import PostModelSerializer, AuthorModelSerializer

# Create your views here.

class PostViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Post.objects.all()

    serializer_class = PostModelSerializer

    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        '''save the author'''
        post = serializer.save()
        author = self.request.user
        Author.objects.create(author=author, post=post)

    def retrieve(self,request, *args, **kwargs):
        '''bring the author'''
        instance = self.get_object()
        author = Author.objects.get(post=instance.pk)
        serializer = AuhtorModelSerializer(author)
        return Response(serializer.data)

    def get_permissions(self):
        permissions = [IsAuthenticated] 

        if self.action in ['update', 'partial_update', 'destroy']:
            permissions.append(IsAuthor)
        
        return [permission() for permission in permissions]

    def list(self,request,*args,**kwargs):
        """list all post data with authors"""

        queryset = Author.objects.all() 
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = AuthorModelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AuthorModelSerializer(queryset, many=True)
        return Response(serializer.data)