from rest_framework import serializers
from user.models import Account as UserAccountModel


class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField()
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        return UserAccountModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        return instance
