from django.db import transaction
from djmoney.money import Money
from rest_framework import serializers
from django.conf import settings

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        try:
            user = self.context['request'].user
        except (AttributeError, KeyError):
            user = None

        if not user:
            raise serializers.ValidationError("Auth is required")

        if not attrs.get('from_user'):
            attrs['from_user'] = user
        elif attrs['from_user'] != user and not user.is_superuser:
            raise serializers.ValidationError("Operation not allowed")

        if attrs['from_user'] == attrs['to_user']:
            raise serializers.ValidationError(
                "'From' and 'to' users shold be different"
            )

        return attrs

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        amount = instance.amount
        with transaction.atomic():
            instance.from_user.balance_change(-amount)
            instance.to_user.balance_change(amount)
            instance.save()

        return instance

    class Meta:
        model = Transaction
        fields = ['from_user', 'to_user', 'amount', 'amount_currency', 'date']
        extra_kwargs = {
            'from_user': {'required': False},
            'amount': {'required': True}
        }
