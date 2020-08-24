from snippets.models import Snippet
from users.serializers import AccountSerializer as UserAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Account as UsersAccountModel


class UsersAccount(APIView):

    def get(self, request):
        for user in UsersAccountModel.objects.all():
            print(user)

        return Response()

    def post(self, request):
        requestData = request.data
        serializer = UserAccountSerializer(data=requestData)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
