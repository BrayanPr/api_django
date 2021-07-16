from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'city','profile_picture_url', 'header_img_url', 'country', 'followers', 'likes', 'posts']

class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        
        instance.save()

        profile.age = profile_data.get('age', profile.age)
        profile.city = profile_data.get('city', profile.city)
        profile.profile_picture_url = profile_data.get('profile_picture_url', profile.profile_picture_url)
        profile.header_img_url = profile_data.get('header_img_url', profile.header_img_url)
        profile.country = profile_data.get('country', profile.country)
        profile.followers = profile_data.get('followers', profile.followers)
        profile.likes = profile_data.get('likes', profile.likes)
        profile.posts = profile_data.get('posts', profile.posts)
        profile.save()

        return instance
class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=['username']

class ProfileCompletionSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=4,
        max_length=150,
        allow_blank=False,
    validators=[UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(
        max_length=150,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all())])

    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    age = serializers.IntegerField()

    profile_picture_url = serializers.ImageField()
    header_img_url = serializers.ImageField()
    
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    likes = serializers.IntegerField()
    followers = serializers.IntegerField()
    posts = serializers.IntegerField()

    def create(self,data):
        user = User.objects.get()
        user = User.objects.create_user(
            username=data['username'], 
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email']
        )
        profile = Profile(user=user)
        profile.is_verified=False
        
        profile.save()