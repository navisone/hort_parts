from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=300)
    info = models.TextField("Info", null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    url = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to="catalog_image/", null=True, blank=True)
    source_category = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.url)

    def get_absolute_url(self):
        return reverse('hort:product_list', args=[self.url])

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Commercial(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL, related_name="commercial_category", null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    url = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to="commercial_image/", null=True, blank=True)
    source_commercial = models.CharField(max_length=300, null=True, blank=True)
    source_category = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = "Commercial"
        verbose_name_plural = "Commercials"


class Product(models.Model):
    source_id = models.CharField(max_length=300, null=True, blank=True)
    article = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL, related_name="product_category", null=True, blank=True)
    commercial = models.ForeignKey(Commercial,
                                   on_delete=models.SET_NULL, related_name="product_commercial", null=True, blank=True)
    specification = models.CharField(max_length=300, null=True, blank=True)
    advanced_description = models.TextField("Advanced description", null=True, blank=True)
    is_active = models.BooleanField(default=1, null=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    source_commercial = models.CharField(max_length=300, null=True, blank=True)
    source_category = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.article)

    def get_absolute_url(self):
        return reverse('hort:product_detail', args=[self.category.url, self.slug])

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="product_image")
    source_product = models.CharField(max_length=300, null=True, blank=True)
    image_url = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"


class ContentCategory(models.Model):
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ContentCategory"
        verbose_name_plural = "ContentCategories"


class Content(models.Model):
    alias = models.SlugField(max_length=300, unique=True)
    published = models.BooleanField(default=0)
    main_image = models.ImageField(upload_to="content/main_image/", blank=True, null=True)
    category = models.ForeignKey(
        ContentCategory, on_delete=models.SET_NULL, related_name="content_category", null=True, blank=True)
    title = models.CharField(max_length=300, null=True)
    full_text = models.TextField(null=True)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"


class Cross(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cross_product", null=True, blank=True)
    brand = models.CharField(max_length=500, null=True, blank=True)
    article_nr = models.CharField(max_length=500, null=True, blank=True)
    product = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.article_nr

    class Meta:
        verbose_name = "Cross"
        verbose_name_plural = "Crosses"


class Applicability(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="applicability_product", null=True, blank=True)
    vehicle = models.CharField(max_length=250, null=True, blank=True)
    modification = models.CharField(max_length=250, null=True, blank=True)
    engine = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    product = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Applicability"
        verbose_name_plural = "Applicabilities"


class Description(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="description_product", null=True, blank=True)
    property = models.CharField(max_length=500, null=True, blank=True)
    value = models.CharField(max_length=500, null=True, blank=True)
    product = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"
