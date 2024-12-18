from rest_framework import serializers
from django import forms
from django_advanced.post_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
