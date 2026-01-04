from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OpenPadSerializer, SavePadSerializer
from .services import open_or_create_pad, save_pad


class OpenPadView(APIView):
    def post(self, request):
        serializer = OpenPadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = open_or_create_pad(serializer.validated_data["key"])
        return Response({"content": content}, status=status.HTTP_200_OK)


class SavePadView(APIView):
    def put(self, request):
        serializer = SavePadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        save_pad(
            serializer.validated_data["key"],
            serializer.validated_data["content"]
        )
        return Response({"status": "saved"}, status=status.HTTP_200_OK)
