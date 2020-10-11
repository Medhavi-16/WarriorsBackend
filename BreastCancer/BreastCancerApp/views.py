from django.shortcuts import render
from BreastCancerApp.models import Quotes,Stories
from BreastCancerApp.serializers import GetQuotesSerializer,GetStoriesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class GetQuotesView(APIView):
    def get(self, request):
        model = Quotes.objects.all().order_by('quote')
        serializer = GetQuotesSerializer(model, many= True)
        return Response(serializer.data)

class GetStoriesView(APIView):
    def get(self, request):
        model=Stories.objects.all().order_by('-time')
        serializer = GetStoriesSerializer(model, many=True)
        return Response(serializer.data)

