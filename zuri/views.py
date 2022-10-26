from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status



class Home(GenericAPIView):
    def get(self, request):
        return Response({"message":"Hello World"}, status=status.HTTP_200_OK)
    