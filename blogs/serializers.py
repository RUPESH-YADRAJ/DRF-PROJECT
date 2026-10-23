from rest_framework import serializers
from .models import Blog, Comment


class CommentSerialier(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
  comments = CommentSerialier(many = True, read_only = True)  ## the comments must be related_name of comment model
  class Meta:
    model = Blog
    fields = '__all__'
