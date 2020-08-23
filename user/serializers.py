from rest_framework import serializers
from user.models import Account as UserAccountModel


class AccountSerializer(serializers.ModelSerializer):
    print(UserAccountModel)

    class Meta:
        model = UserAccountModel
