
""" Users Serializers """

#Django REST framework
from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """ Profile model serializer """

    class Meta:
        model = Profile
        fields = ['age', 'city', 'country', 'followers', 'likes', 'posts', 'header_img_url', 'profile_picture_url']


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name', 'profile']

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
        profile.country = profile_data.get('country', profile.country)
        profile.header_img_url = profile_data.get('header_img_url', profile.header_img_url)
        profile.profile_picture_url = profile_data.get('profile_picture_url', profile.profile_picture_url)
        profile.save()

        return instance


class NewUserSerializer(serializers.ModelSerializer):
    """ Return the data for a new user """

    class Meta:
        model = User
        fields = ['username']