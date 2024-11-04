from django.contrib.auth.models import User
from rest_framework import serializers

from app_menu.models import CategoryModel, ProductModel, CommentModel


class CategorySerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())

    class Meta:
        model = ProductModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())

    class Meta:
        model = CommentModel
        fields = '__all__'
