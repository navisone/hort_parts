from modeltranslation.translator import register, TranslationOptions
from .models import Product, ContentCategory, Category, Content, Commercial


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'info', 'comment')


@register(Commercial)
class CommercialTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'comment', 'advanced_description')


@register(ContentCategory)
class CatalogCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(Content)
class ContentTypeMethodTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')

