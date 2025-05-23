from .models import (Main, About, Meal, SupplementItem,
                     RestaurantInfo, AboutUs, BestSeller)
from modeltranslation.translator import TranslationOptions,register


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(BestSeller)
class BestSellerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Meal)
class MealTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SupplementItem)
class SupplementItemTranslationOptions(TranslationOptions):
    fields = ('item',)


@register(RestaurantInfo)
class RestaurantInfoTranslationOptions(TranslationOptions):
    fields = ('title',)
