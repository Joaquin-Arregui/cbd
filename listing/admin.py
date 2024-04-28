from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

from .models import Amenity, Neighborhood, Host, User, Review, Listing

# Neo4j models registration
class AmenityAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)

class NeighborhoodAdmin(dj_admin.ModelAdmin):
    list_display = ("name", "neighborhood_id")

class HostAdmin(dj_admin.ModelAdmin):
    list_display = ("name", "host_id", "superhost", "location", "image")

class UserAdmin(dj_admin.ModelAdmin):
    list_display = ("name", "user_id")

class ReviewAdmin(dj_admin.ModelAdmin):
    list_display = ("review_id", "date", "comments")

class ListingAdmin(dj_admin.ModelAdmin):
    list_display = ("listing_id", "name", "price", "property_type", "accommodates", "bedrooms", "bathrooms", "availability_365", "weekly_price", "cleaning_fee")

# Register the Neo4j models with NeoModelAdmin
neo_admin.register(Amenity, AmenityAdmin)
neo_admin.register(Neighborhood, NeighborhoodAdmin)
neo_admin.register(Host, HostAdmin)
neo_admin.register(User, UserAdmin)
neo_admin.register(Review, ReviewAdmin)
neo_admin.register(Listing, ListingAdmin)
