from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Main(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='main_page_image/')
    restaurant_name = models.CharField(max_length=32)
    description = models.TextField()
    title_address = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    title_phone = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')


class AboutUs(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about_images/')
    image2 = models.ImageField(upload_to='about_images/')


class BestSeller(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about_images/')
    image2 = models.ImageField(upload_to='about_images/')


class Menu(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)


class Category(models.Model):
    category_name = models.CharField(max_length=32)


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    ingredient = models.TextField()
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)


class Supplement(models.Model):
    supplement_name = models.CharField(max_length=32)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)


class SupplementItem(models.Model):
    item = models.CharField(max_length=32)
    price = models.PositiveSmallIntegerField()
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)


class RestaurantImage(models.Model):
    title = models.CharField(max_length=32)


class Image(models.Model):
    image = models.ImageField(upload_to='restaurant_images/')
    restaurant = models.ForeignKey(RestaurantImage, on_delete=models.CASCADE)


class RestaurantInfo(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    region = models.CharField(max_length=128)
    title_contact = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')
    email = models.EmailField(unique=True)


class Day(models.Model):
    day = models.CharField(max_length=8)


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day_start')
    end_day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day_end')
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')
