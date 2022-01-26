from django.urls import path
from . import views

app_name = 'hort'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('warranty/', views.WarrantyView.as_view(), name='warranty'),
    path('download/', views.download, name='download'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('<slug:category_slug>/detail\u003furl=<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.Search.as_view(), name='search'),

]
