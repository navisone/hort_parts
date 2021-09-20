from django.urls import path
from . import views
app_name = 'hort'

urlpatterns = [
    path('', views.index, name='home'),

]
