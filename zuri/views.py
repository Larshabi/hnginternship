from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status



class Home(GenericAPIView):
    def get(self, request):
        data = {
        "slackUsername":"Lash", "backend":True, "age":22, "bio":"My name is Lasabi Olalekan Muqeet."}
        return Response(data, status=status.HTTP_200_OK)
    