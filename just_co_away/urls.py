from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('listings', views.listings, name = 'listings'),
    path('listing/<int:pk>/', views.listing_detail, name = 'listing_detail'),
    path('meallistings', views.meallistings, name = 'meallistings'),
    path('meallisting/<int:pk>/', views.meallisting_detail, name = 'meallisting_detail'),
    path('contributors', views.contributors, name = 'contributors'),
]
