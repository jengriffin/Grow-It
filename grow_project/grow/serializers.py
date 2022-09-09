from rest_framework import serializers
from .models import Plant, Blog, User


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    # blogs = serializers.HyperlinkedRelatedField(
    #     view_name='blog_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Plant
        fields = ('id', 'name', 'image', 'info', )


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    plant = serializers.HyperlinkedRelatedField(
        view_name='plant_detail',
        read_only=True
    )
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    class Meta:
        model = Blog
        fields = ('id', 'date', 'title', 'body', 'plant',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'blogs',)
