from django.shortcuts import render
from django.utils import timezone
from.models import Listing, MealListing
from django.shortcuts import render, get_object_or_404
from .forms import ListingForm
from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
    homepage = loader.get_template('just_co_away/homepage.html')
    return HttpResponse(homepage.render())

def contributors(request):
    contributors = loader.get_template('just_co_away/contributors.html')
    return HttpResponse(contributors.render())

def listings(request):
    listings_list = Listing.available_objects.filter(published_date__lte = timezone.now())
    page = request.GET.get('page', 1)
    
    paginator = Paginator(listings_list, 6)

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    return render(request, 'just_co_away/listings.html', 
    {'listings': listings, 
    'api_key': settings.GOOGLE_MAPS_API_KEY,
    })

def meallistings(request):
    meallistings_list = MealListing.available_objects.filter(published_date__lte = timezone.now())
    page = request.GET.get('page', 1)
    
    paginator = Paginator(meallistings_list, 6)

    try:
        meallistings = paginator.page(page)
    except PageNotAnInteger:
        meallistings = paginator.page(1)
    except EmptyPage:
        meallistings = paginator.page(paginator.num_pages)

    return render(request, 'just_co_away/meallistings.html', 
    {'meallistings': meallistings, 
    'api_key': settings.GOOGLE_MAPS_API_KEY,
    })

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk = pk)
    return render(request, 'just_co_away/listing_detail.html', {'listing': listing})

def meallisting_detail(request, pk):
    meallisting = get_object_or_404(MealListing, pk = pk)
    return render(request, 'just_co_away/meallisting_detail.html', {'meallisting': meallisting})
