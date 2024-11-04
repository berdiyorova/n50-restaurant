from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from app_menu.models import CategoryModel, ProductModel, CommentModel
from app_menu.serializers import CategorySerializer, ProductSerializer, CommentSerializer


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
        category = get_object_or_404(CategoryModel, pk=self.kwargs.get('pk'))
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
        ProductModel.objects.filter(pk=self.kwargs.get('pk')).delete()
        return Response(
            {
                'success': True,
                'message': 'The product object was deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated,]
    lookup_url_kwarg = 'pk'

    def get_queryset(self, **kwargs):
        return CommentModel.objects.filter(product__pk=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated,]
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return CommentModel.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        CommentModel.objects.filter(pk=self.kwargs.get('pk')).delete()
        return Response(
            {
                'success': True,
                'message': 'The comment object was deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )
