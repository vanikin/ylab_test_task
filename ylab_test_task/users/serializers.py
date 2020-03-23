from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'email', 'balance', 'balance_currency', 'password']
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}
