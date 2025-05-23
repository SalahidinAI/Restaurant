from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Main(models.Model):
    image = models.ImageField(upload_to='main_page_image/')
    restaurant_name = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=64)
    phone = PhoneNumberField(region='KG')


class About(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about_images/')
    image2 = models.ImageField(upload_to='about_images/')

    class Meta:
        abstract = True


class AboutUs(About):
    pass


class BestSeller(About):
    pass


class MealImage(models.Model):
    image = models.ImageField(upload_to='meal_images/')


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    images = models.ForeignKey(MealImage, on_delete=models.CASCADE)


class Supplement(models.Model):
    supplement_items = models.ForeignKey(Meal, on_delete=models.CASCADE)


class SupplementItem(models.Model):
    item = models.CharField(max_length=32)
    price = models.PositiveSmallIntegerField()
    supplements = models.ForeignKey(Supplement, on_delete=models.CASCADE)


class Dessert(Meal):
    pass


class HotDrink(Meal):
    pass


class ColdDrink(Meal):
    pass


class NationalFood(Meal):
    pass


class EasternCuisine(Meal):
    pass


class FastFood(Meal):
    pass


class RestaurantImage(models.Model):
    title = models.CharField(max_length=32)


class Image(models.Model):
    image = models.ImageField(upload_to='restaurant_images/')
    restaurant = models.ForeignKey(RestaurantImage, on_delete=models.CASCADE)


class RestaurantInfo(models.Model):
    title = models.CharField(max_length=64)
    region = models.CharField(max_length=128)
    phone = PhoneNumberField(region='KG')
    email = models.EmailField(unique=True)


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    DAYS_CHOICES = (
        ('пн', 'пн'),
        ('вт', 'вт'),
        ('ср', 'ср'),
        ('чт', 'чт'),
        ('пт', 'пт'),
        ('сб', 'сб'),
        ('вс', 'вс'),
    )
    working_days = MultiSelectField(choices=DAYS_CHOICES, max_length=16)
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=32)
    phone = PhoneNumberField(region='KG')
