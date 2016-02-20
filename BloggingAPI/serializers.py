from rest_framework import serializers
from .models import *

#Author Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', )

#Post Serializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
