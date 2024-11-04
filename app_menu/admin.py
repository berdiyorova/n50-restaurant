from django.contrib import admin

from app_menu.models import CategoryModel, ProductModel, CommentModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name', 'description')


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category__name')
    list_filter = ('category', 'price')
    search_fields = ('id', 'name', 'description')


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('user', 'product', 'created_at', 'stars_given')
    search_fields = ('id', 'comment', 'user__username', 'product__name')
