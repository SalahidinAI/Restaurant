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

    def __str__(self):
        return f'{self.title}'


class AboutUs(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about_images/')
    image2 = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return f'{self.title}'


class BestSeller(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'


class BestSellerImage(models.Model):
    image = models.ImageField(upload_to='best_seller_images/')
    best_seller = models.ForeignKey(BestSeller, on_delete=models.CASCADE, related_name='best_photos')

    def __str__(self):
        return f'{self.best_seller}'


class Menu(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.category_name}'


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    ingredient = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='meals')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_images')

    def __str__(self):
        return f'{self.meal}'


class Supplement(models.Model):
    supplement_name = models.CharField(max_length=32)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='supplements')

    def __str__(self):
        return f'{self.meal}'


class SupplementItem(models.Model):
    item = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'{self.item}'


class RestaurantImage(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(upload_to='restaurant_images/')
    restaurant = models.ForeignKey(RestaurantImage, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.restaurant}'


class RestaurantInfo(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    title_region = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    title_schedule = models.CharField(max_length=32)
    title_contact = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.title}'


class Day(models.Model):
    day = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.day}'


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day_start')
    end_day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day_end')
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE, related_name='schedule')

    def __str__(self):
        return f'{self.restaurant}'


class Contact(models.Model):
    name = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')

    def __str__(self):
        return f'{self.name}'
