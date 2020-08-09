from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import RealtorSerializer
from .models import Realtor


class RealtorListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()
    pagination_class = None


class RealtorView(RetrieveAPIView):
    serializer_class = RealtorSerializer
    queryset = Realtor.objects.all()


class TopSellerView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RealtorSerializer
    pagination_class = None
    queryset = Realtor.objects.filter(top_seller=True)
