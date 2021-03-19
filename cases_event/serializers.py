
from rest_framework import serializers
from .models import PartisipantPresent

class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartisipantPresent
        fields = [
                'category',
                'present_in_category'
            ]
