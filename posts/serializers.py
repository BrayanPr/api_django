from rest_framework import serializers

from posts.models import Post, Author

from django.contrib.auth.models import User

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image', 'title', 'likes', 'created_at']

class GetAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class AuthorModelSerializer(serializers.ModelSerializer):

    author = GetAuthorSerializer(read_only=True) 
    class Meta:
        model = Author
        fields = ['author', 'post']
        depth=1