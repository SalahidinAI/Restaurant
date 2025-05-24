from .models import (Main, Menu, Day, Meal, Category, SupplementItem,
                     RestaurantImage, Supplement, RestaurantInfo, AboutUs,
                     BestSeller)
from modeltranslation.translator import TranslationOptions, register


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'title_address', 'title_phone')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'description')


@register(BestSeller)
class BestSellerTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'description')


@register(Menu)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('label', 'title')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Meal)
class MealTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'ingredient')


@register(Supplement)
class SupplementTranslationOptions(TranslationOptions):
    fields = ('supplement_name',)


@register(SupplementItem)
class SupplementItemTranslationOptions(TranslationOptions):
    fields = ('item',)


@register(RestaurantImage)
class RestaurantImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(RestaurantInfo)
class RestaurantInfoTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'title_region', 'title_schedule', 'title_contact')


@register(Day)
class DayTranslationOptions(TranslationOptions):
    fields = ('day',)
