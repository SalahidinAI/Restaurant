from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters


class MainAPIView(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class AboutUsAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class BestSellerAPIView(generics.ListAPIView):
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializer


class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class MealAPIView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]


class RestaurantImageAPIView(generics.ListAPIView):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer


class RestaurantInfoAPIView(generics.ListAPIView):
    queryset = RestaurantInfo.objects.all()
    serializer_class = RestaurantInfoSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
