from rest_framework import serializers
from .models import *


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['id', 'title', 'image', 'restaurant_name', 'description',
                  'title_address', 'address', 'title_phone', 'phone']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'label', 'title', 'description', 'image1', 'image2']


class BestSellerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellerImage
        fields = ['id', 'image']


class BestSellerSerializer(serializers.ModelSerializer):
    best_photos = BestSellerImageSerializer(many=True, read_only=True)

    class Meta:
        model = BestSeller
        fields = ['id', 'label', 'title', 'description', 'best_photos']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'label', 'title']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class MealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields = ['id', 'image']


class SupplementItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplementItem
        fields = ['id', 'item', 'price']


class SupplementSerializer(serializers.ModelSerializer):
    items = SupplementItemSerializer(many=True, read_only=True)

    class Meta:
        model = Supplement
        fields = ['id', 'supplement_name', 'items']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class RestaurantImageSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = RestaurantImage
        fields = ['id', 'title', 'images']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'day']


class ScheduleSerializer(serializers.ModelSerializer):
    start_day = DaySerializer()
    end_day = DaySerializer()
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'end_time', 'start_day', 'end_day']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    supplements = SupplementSerializer(many=True, read_only=True)
    meal_images = MealImageSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'ingredient', 'price', 'supplements', 'meal_images']


class CategoryDetailSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'meals']


class RestaurantInfoSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = RestaurantInfo
        fields = ['id', 'label', 'title', 'title_region', 'region', 'title_schedule',
                  'schedule', 'title_contact', 'phone', 'email']
