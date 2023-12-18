from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.api.serializers import user_serializer
from apps.users.models import User


class user_view(APIView):
    model = User
    serializer_class = user_serializer

    def get(self, request):
        users = self.model.objects.all()

        users_serializer = self.serializer_class(users, many=True)

        return Response(status=status.HTTP_200_OK, data=users_serializer.data)

    def post(self, request):
        body = request.data
        user_serializer = self.serializer_class(data=body)

        if not user_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=user_serializer.errors)

        user_serializer.save()

        return Response(status=status.HTTP_201_CREATED, data={
            "status": True,
            "message": "Usuario creado",
            "data": user_serializer.data
        })


class user_detail_view(APIView):
    model = User
    queryset = User.objects.filter
    serializer_class = user_serializer

    def get(self, request, pk):
        user = self.queryset(id=pk).first()
        user_serializer = self.serializer_class(user)
        return Response(status=status.HTTP_200_OK, data=user_serializer.data)

    def put(self, request, pk):
        body = request.data

        user = self.queryset(id=pk).first()
        user_serializer = self.serializer_class(user, data=body)

        if not user_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=user_serializer.errors)

        user_serializer.save()
        return Response(status=status.HTTP_200_OK, data=user_serializer.data)

    def delete(self, request, pk):
        User = self.queryset(id=pk).first()

        User.delete()

        return Response(status=status.HTTP_200_OK, data="Eliminado")
