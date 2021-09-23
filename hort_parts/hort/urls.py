from django.urls import path
from . import views
app_name = 'hort'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('contact/', views.ContactsView.as_view(), name='contacts'),
    path('warranty/', views.WarrantyView.as_view(), name='warranty'),

]
