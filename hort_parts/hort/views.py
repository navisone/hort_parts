from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def index(request):
    return render(request, 'hort_parts/index.html')


class NewsView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=1)
    context_object_name = 'news_list'
    paginate_by = 10
    template_name = 'hort_parts/news/news_list.html'


class NewsDetailView(DetailView):
    model = Content
    slug_field = 'alias'
    context_object_name = 'news_detail'
    template_name = 'hort_parts/news/news_detail.html'


class AboutUsView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=2)
    context_object_name = 'about_list'
    template_name = 'hort_parts/about.html'


class ContactsView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=3)
    context_object_name = 'contacts_list'
    template_name = 'hort_parts/contact.html'


class WarrantyView(ListView):
    model = Content
    queryset = Content.objects.filter(category_id=4)
    context_object_name = 'warranty_list'
    template_name = 'hort_parts/warranty.html'

