

from rest_framework import serializers
from .models import Plant, Blog, User


class PlantSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Plant
        fields = "__all__"


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    plant = serializers.HyperlinkedRelatedField(
        view_name='plant_detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    print("in blog serializer")

    class Meta:
        model = Blog
        fields = ('id', 'plant', 'date', 'title', 'body',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'blogs',)
