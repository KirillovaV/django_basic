from django.urls import path

import adminapp.views.user_views as user
import adminapp.views.category_views as category
import adminapp.views.product_views as product

app_name = 'adminapp'

urlpatterns = [
    path('users/read/', user.UsersListView.as_view(), name='users'),
    path('users/create/', user.UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', user.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UserDeleteView.as_view(), name='user_delete'),

    path('categories/read/', category.CategoriesListView.as_view(), name='categories'),
    path('categories/create/', category.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>/', category.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', category.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/read/<int:pk>/', product.ProductReadView.as_view(), name='product_read'),
    path('products/delete/<int:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),

    path('products/create/category/<int:pk>/', product.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', product.products, name='products'),
    path('products/update/<int:pk>/', product.product_update, name='product_update'),
]
