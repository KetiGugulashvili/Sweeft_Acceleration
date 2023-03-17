from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from .serializers import RandomUrlSerializers, CustomUrlSerializers
from .models import Url
from django.http import HttpResponseRedirect


class ShortenUrl(APIView):
    def post(self, request):
        serializer = RandomUrlSerializers(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


"""As we don't have the user model, we cannot validate whether the user is premium or not, 
thus, I thought it would be better to have two different endpoints, 
even though serializers and views for both look alike"""
class CustomizeUrl(APIView):
    def post(self, request):
        serializer = CustomUrlSerializers(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class Redirect(APIView):
    def get(self, request, shortened_part):
        try:
            url = get_object_or_404(Url, shortened_part=shortened_part)
            url.times_accessed += 1
            url.save()
            return HttpResponseRedirect(url.long_url)
        except Url.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListOfUrls(ListAPIView):
        queryset = Url.objects.all()
        serializer_class = RandomUrlSerializers
