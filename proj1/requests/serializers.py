from rest_framework import serializers
from . import models


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Request