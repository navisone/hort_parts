from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_title = 'Hort.parts'
admin.site.site_header = 'Hort.parts'


class ContentAdminForm(forms.ModelForm):
    full_text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    full_text_uk = forms.CharField(widget=CKEditorUploadingWidget())
    full_text_en = forms.CharField(widget=CKEditorUploadingWidget())
    full_text_de = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    info_ru = forms.CharField(widget=CKEditorUploadingWidget())
    info_uk = forms.CharField(widget=CKEditorUploadingWidget())
    info_en = forms.CharField(widget=CKEditorUploadingWidget())
    info_de = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'url', 'image')
    list_display_links = ('name',)
    readonly_fields = ('get_image',)
    save_on_top = True
    form = CategoryAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} widht="50" height="60"')

    get_image.short_description = 'image'


@admin.register(ContentCategory)
class ContentCategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Content)
class ContentAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'alias', 'category_id', 'main_image', 'published')
    list_filter = ('category_id',)
    list_display_links = ('title',)
    readonly_fields = ('get_main_image',)
    save_on_top = True
    form = ContentAdminForm

    def get_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} widht="50" height="60"')

    get_main_image.short_description = 'image'


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'article', 'specification', 'category', 'slug', 'is_active')
    list_display_links = ('name', 'article',)
    search_fields = ('name', 'article',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image_url')
    list_display_links = ('product',)
