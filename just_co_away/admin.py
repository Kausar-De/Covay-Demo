from django.contrib import admin

from django.contrib import admin
from .models import Listing, MealListing

admin.site.register(Listing)
admin.site.register(MealListing)
