from rest_framework import serializers
from .models import Post

#Serializing data with serializers.Serializer
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(default='')

#     def create(self, validated_data):
#         return Post.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',validated_data.title)
#         instance.author = validated_data.get('author',validated_data.author)
#         instance.email = validated_data.get('email',validated_data.email)
#         return Post.objects.update(instance, validated_data)

#Serializing data with serializers.ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','email']