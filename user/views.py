from snippets.models import Snippet
from user.serializers import AccountSerializer as UserAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserAccount(APIView):

    UserAccountSerializer()
    def get(self, request):
        return Response()
