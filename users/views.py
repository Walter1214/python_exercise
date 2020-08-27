from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import AccountSerializer as UserAccountSerializer
from users.models import Account as UsersAccountModel


class UsersAccount(APIView):

    def get(self, request):
        for user in UsersAccountModel.objects.all():
            print(user)

        return Response()

    def post(self, request):
        requestData = request.data
        # try:
        serializer = UserAccountSerializer(data=requestData)
        exitAccount = UsersAccountModel.objects.filter(
            name=requestData['name'])
        print('$$$$4', exitAccount)
        # except expression as identifier:
        #     pass
        # if serializer.is_valid():
        #     serializer.save()

        # return Response(serializer.data)
        return Response()
