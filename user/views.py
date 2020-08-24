from snippets.models import Snippet
from user.serializers import AccountSerializer as UserAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Account as UserAccountModel


class UserAccount(APIView):

    def get(self, request):
        for user in UserAccountModel.objects.all():
            print(user)

        return Response()

    def post(self, request):
        requestData = request.data
        serializer = UserAccountSerializer(data=requestData)



        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
