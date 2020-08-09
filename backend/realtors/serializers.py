from rest_framework import serializers
from . import models


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Realtor
        fields = "__all__"
