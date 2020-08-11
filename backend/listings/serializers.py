from rest_framework import serializers
from .models import Listing, Photo


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'price',
                  'sale_type', 'home_type', 'bedrooms',
                  'bathrooms', 'sqft', 'photo_main', 'slug']


class ListingDetailSerializer(ListingSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
        lookup_field = 'slug'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
