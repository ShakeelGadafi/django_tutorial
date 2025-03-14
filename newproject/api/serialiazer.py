#tell python to tranfer our modle data into jason data in our api
from rest_framework import serializers
from .models import User

class UserSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'