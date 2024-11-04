from rest_framework import serializers

from app_menu.models import CategoryModel, ProductModel


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
