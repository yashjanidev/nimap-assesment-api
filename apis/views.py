from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apis.models import Clients
from apis.serializer import ClientSerializer


class ClientLists(APIView):
    def get(self, request):
        clients = Clients.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientCreate(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientsData(APIView):

    def get_client_by_pk(self, pk):
        try:
            return Clients.objects.get(pk=pk)

        except:
            return Response({
                "error": "Client doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        clients = self.get_client_by_pk(pk)
        serializer = ClientSerializer(clients)
        return Response(serializer.data)

    def put(self, request, pk):
        clients = self.get_client_by_pk(pk)
        serializer = ClientSerializer(clients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        clients = self.get_client_by_pk(pk)
        clients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
