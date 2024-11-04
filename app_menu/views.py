from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from app_menu.models import CategoryModel, ProductModel
from app_menu.serializers import CategorySerializer, ProductSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAdminUser,]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsAdminUser,]
    lookup_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(CategoryModel, pk=kwargs.get('pk'))
        category.delete()
        return Response(
            {
                'success': True,
                'message': 'The category object was deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAuthenticated()]

        return [IsAdminUser()]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminUser,]
    lookup_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        ProductModel.objects.filter(pk=kwargs.get('pk')).delete()
        return Response(
            {
                'success': True,
                'message': 'The product object was deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )



