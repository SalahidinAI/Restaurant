from rest_framework import serializers
from .models import *


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class BestSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSeller
        fields = '__all__'


class MealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields = '__all__'


class SupplementItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplementItem
        fields = '__all__'


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'


class HotDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotDrink
        fields = '__all__'


class ColdDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColdDrink
        fields = '__all__'


class NationalFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalFood
        fields = '__all__'


class EasternCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasternCuisine
        fields = '__all__'


class FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFood
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
