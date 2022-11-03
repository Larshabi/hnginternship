from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework import status
from .serializer import OperationsSerializer
from rest_framework.permissions import AllowAny



class Home(GenericAPIView):
    def get(self, request):
        data = {
        "slackUsername":"Lash", "backend":True, "age":22, "bio":"My name is Lasabi Olalekan Muqeet."}
        return Response(data, status=status.HTTP_200_OK)
    
class Operation(CreateAPIView):
    serializer_class = OperationsSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    