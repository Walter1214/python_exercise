from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tutorial.utils.exceptions import AccountRepeat as AccountRepeatException, ValidateFail, Common as CommonException
from rest_framework.exceptions import APIException
from tutorial.constants.message import Success as MessageSuccess

from users.serializers import AccountSerializer as UserAccountSerializer
from users.models import Account as UsersAccountModel


class UsersAccount(APIView):

    def get(self, request):
        for user in UsersAccountModel.objects.all():
            print(user)

        return Response()

    def post(self, request):

        requestData = request.data
        exitAccount = UsersAccountModel.objects.filter(
            name=requestData['name'])
        if exitAccount:
            raise AccountRepeatException()
        serializer = UserAccountSerializer(data=requestData)
        print('%%%%', serializer)

        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                raise CommonException(
                    {'code': 9999, 'message': 'internal error'})
        else:
            raise ValidateFail()

        return Response(MessageSuccess)
