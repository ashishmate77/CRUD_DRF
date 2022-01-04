from DRF_APP.models import UserReg
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReg
        fields = '__all__'
