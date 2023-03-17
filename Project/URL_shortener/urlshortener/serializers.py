from rest_framework import serializers
from .models import Url
from django.urls import reverse


class RandomUrlSerializers(serializers.ModelSerializer):
    long_url = serializers.URLField(required=True, max_length=250)
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = "__all__"
        read_only_fields = ["shortened_part", "time_of_creation", "times_accessed"]

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('redirect', args=[obj.shortened_part]))


"""As we don't have the user model, we cannot validate whether the user is premium or not, 
thus, I thought it would be better to have two different endpoints, 
even though serializers and views for both look alike"""
class CustomUrlSerializers(serializers.ModelSerializer):
    long_url = serializers.URLField(required=True)
    shortened_part = serializers.CharField(required=True, max_length=7)
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = "__all__"
        read_only_fields = ["time_of_creation", "times_accessed"]

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('redirect', args=[obj.shortened_part]))
