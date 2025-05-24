from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *


class GeneralMedia:
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Main)
class MainAdmin(TranslationAdmin, GeneralMedia):
    pass


class MealImageInline(admin.TabularInline):
    model = MealImage
    extra = 1


@admin.register(Meal)
class MealAdmin(TranslationAdmin, GeneralMedia):
    inlines = [MealImageInline]
    pass


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1


@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(TranslationAdmin, GeneralMedia):
    inlines = [ScheduleInline]
    pass


class SupplementItemInline(TranslationInlineModelAdmin, admin.TabularInline, GeneralMedia):
    model = SupplementItem
    extra = 1


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin, GeneralMedia):
    pass


class BestSellerImageInline(admin.TabularInline):
    model = BestSellerImage
    extra = 1


@admin.register(BestSeller)
class BestSellerAdmin(TranslationAdmin, GeneralMedia):
    inlines = [BestSellerImageInline]
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Day)
class DayAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Menu)
class MenuAdmin(TranslationAdmin, GeneralMedia):
    pass


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(RestaurantImage)
class RestaurantImageAdmin(TranslationAdmin, GeneralMedia):
    inlines = [ImageInline]


@admin.register(Supplement)
class SupplementAdmin(TranslationAdmin, GeneralMedia):
    inlines = [SupplementItemInline]


admin.site.register(Contact)
