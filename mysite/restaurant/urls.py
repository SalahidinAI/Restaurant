from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainAPIView.as_view(), name='main_list'),
    path('about/', AboutUsAPIView.as_view(), name='about_list'),
    path('best/', BestSellerAPIView.as_view(), name='best_list'),
    path('menu/', MenuAPIView.as_view(), name='menu_list'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('interior/', RestaurantImageAPIView.as_view(), name='interior_list'),
    path('info/', RestaurantInfoAPIView.as_view(), name='info_list'),
    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactDetailAPIView.as_view(), name='contact_detail'),
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('meal/', MealAPIView.as_view(), name='meal_list'),
]

