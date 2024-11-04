from django.urls import path

from app_menu import views

app_name = 'menu'

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
    path('products/', views.ProductListCreateView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/<int:pk>/comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]
