from django.urls import path
from . import views
app_name = 'hort'

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('<slug:category_slug>/detail\u003furl=<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.Search.as_view(), name='search'),
    path('about/', views.about, name='about'),
    path('download/', views.download, name='download'),
    path('warranty/', views.warranty, name='warranty'),

]
