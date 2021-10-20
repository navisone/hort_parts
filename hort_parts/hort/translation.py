from modeltranslation.translator import register, TranslationOptions
from .models import Product, ContentCategory, Category, Content


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'info', 'comment')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(ContentCategory)
class CatalogCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(Content)
class ContentTypeMethodTranslationOptions(TranslationOptions):
    fields = ('title', 'full_text')

