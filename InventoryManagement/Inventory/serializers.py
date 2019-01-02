from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.CustomUser

class InventorySerailizer(serializers.ModelSerializer):

    class Meta:
         fields = '__all__'
         model = models.Inventory
