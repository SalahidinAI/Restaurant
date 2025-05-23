from rest_framework import generics
from .models import *
from .serializers import *


class MainAPIView(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


# class AboutAPIView(generics.ListAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer


class AboutUsAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class BestSellerAPIView(generics.ListAPIView):
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializer


class MealImageAPIView(generics.ListAPIView):
    queryset = MealImage.objects.all()
    serializer_class = MealImageSerializer


class SupplementItemAPIView(generics.ListAPIView):
    queryset = SupplementItem.objects.all()
    serializer_class = SupplementItemSerializer


class SupplementAPIView(generics.ListAPIView):
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer


class MealAPIView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class DessertAPIView(generics.ListAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer


class HotDrinkAPIView(generics.ListAPIView):
    queryset = HotDrink.objects.all()
    serializer_class = HotDrinkSerializer


class ColdDrinkAPIView(generics.ListAPIView):
    queryset = ColdDrink.objects.all()
    serializer_class = ColdDrinkSerializer


class NationalFoodAPIView(generics.ListAPIView):
    queryset = NationalFood.objects.all()
    serializer_class = NationalFoodSerializer


class EasternCuisineAPIView(generics.ListAPIView):
    queryset = EasternCuisine.objects.all()
    serializer_class = EasternCuisineSerializer


class FastFoodAPIView(generics.ListAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer


class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RestaurantImageAPIView(generics.ListAPIView):
    queryset = RestaurantImage.objects.all()
    serializer_class = RestaurantImageSerializer


class ScheduleAPIView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class RestaurantInfoAPIView(generics.ListAPIView):
    queryset = RestaurantInfo.objects.all()
    serializer_class = RestaurantInfoSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

