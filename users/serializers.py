from rest_framework import serializers
from users.models import Account as UsersAccountModel


class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        print(validated_data)
        return UsersAccountModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret

class ProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    email = serializers.EmailField()
    last_name = serializers.CharField()