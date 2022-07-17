from rest_framework import serializers
from posts.models import Group, Post, Comment, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created', 'id')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'posts', 'comments')
