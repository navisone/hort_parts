from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def index(request):
    return render(request, 'hort_parts/index.html')


def product_list(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    images = ProductImage.objects.all()
    category = get_object_or_404(Category, url=category_slug)
    products = products.filter(category=category)
    # images = images.filter(product=products).first()
    context = {'category': category, 'categories': categories, 'products': products, 'images': images}
    return render(request, 'hort_parts/product/product_list.html', context)


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    category = get_object_or_404(Category, url=category_slug)
    context = {'category': category, 'product': product}
    return render(request, 'hort_parts/product/product_detail.html', context)


# class ProductView(ListView):
#     model = Product
#     queryset = Product.objects.all()
#     context_object_name = 'product_list'
#     paginate_by = 30
#     template_name = 'hort_parts/product/product_list.html'


# class ProductDetailView(DetailView):
#     model = Product
#     queryset = Product.objects.select_related('product_image').all()
#     context_object_name = 'product_detail'
#     template_name = 'hort_parts/product/product_detail.html'


class Search(ListView):
    paginate_by = 15

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def download(request):
    return render(request, 'hort_parts/product/download.html')


class AboutView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=1)
    context_object_name = 'about_list'
    template_name = 'hort_parts/product/about.html'


class WarrantyView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=2)
    context_object_name = 'warranty_list'
    template_name = 'hort_parts/product/warranty.html'

