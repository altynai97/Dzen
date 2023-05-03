from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Post, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    video_url = serializers.HyperlinkedIdentityField(view_name='post-video', format='html')
    image_url = serializers.HyperlinkedIdentityField(view_name='post-image', format='html')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
