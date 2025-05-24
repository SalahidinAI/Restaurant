from rest_framework import generics
from .models import *
from .serializers import *


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


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MealAPIView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealImageAPIView(generics.ListAPIView):
    queryset = MealImage.objects.all()
    serializer_class = MealImageSerializer


class SupplementItemAPIView(generics.ListAPIView):
    queryset = SupplementItem.objects.all()
    serializer_class = SupplementItemSerializer


class SupplementAPIView(generics.ListAPIView):
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer


class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RestaurantImageAPIView(generics.ListAPIView):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer


class RestaurantInfoAPIView(generics.ListAPIView):
    queryset = RestaurantInfo.objects.all()
    serializer_class = RestaurantInfoSerializer


class ScheduleAPIView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
