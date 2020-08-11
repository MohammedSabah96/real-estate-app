from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Listing, Photo
from .serializers import ListingSerializer, \
    ListingDetailSerializer, PhotoSerializer
from datetime import datetime, timezone
from drf_multiple_model.views import ObjectMultipleModelAPIView


class ListingsView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListingSerializer
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)


class ListingDetailView(ObjectMultipleModelAPIView):
    lookup_field = 'slug'
    pagination_class = None

    def get_querylist(self):
        slug = self.request._request.path.split('/')[-1]
        qs = Listing.objects.filter(slug=slug)
        q = [obj.format_data() for obj in qs]
        q_id = q[0]['id']
        querylist = [
            {'queryset': Listing.objects.order_by('-list_date')
                .filter(is_published=True).filter(slug=slug),
             'serializer_class': ListingDetailSerializer
             },
            {'queryset': Photo.objects.filter(listing_id=q_id), 'serializer_class': PhotoSerializer,
             'label': 'Images'}
        ]
        return querylist


class SearchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)
        price = int(data['price'].replace('$', '').replace(',', ''))
        if price >= 100:
            queryset = queryset.filter(price__gte=price)

        bedrooms = int(data['bedrooms'].replace('+', ''))
        queryset = queryset.filter(bedrooms__gte=bedrooms)

        home_type = data['home_type']
        queryset = queryset.filter(home_type__iexact=home_type)
        bathrooms = int(data['bathrooms'].replace('+', ''))
        queryset = queryset.filter(bathrooms__gte=bathrooms)
        sqft = int(data['sqft'].replace('+', ''))
        if sqft > 0:
            queryset = queryset.filter(sqft__gte=sqft)

        days_passed = int(data['days_listed'])
        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days
            if days_passed != 0:
                if num_days > days_passed:
                    slug = query.slug
                    queryset = queryset.exclude(slug__iexact=slug)

        open_house = data['open_house']
        queryset = queryset.filter(open_house__iexact=open_house)
        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)
