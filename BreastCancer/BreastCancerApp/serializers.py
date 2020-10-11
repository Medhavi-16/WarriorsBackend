from rest_framework import serializers
from BreastCancerApp.models import Quotes,Stories

class GetQuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'

class GetStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stories
        fields = ['id','title','time','writer','writerImageURL','content','imageUrl']

