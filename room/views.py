from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django.utils.text import slugify
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils import ErrorResponse
from cube.models import Cube
from times.actions import start_new_turn
from .models import Room
from .serializers import RoomCreateSerializer, RoomsReadSerializer, RoomReadSerializer


class RoomsView(APIView):

    @swagger_auto_schema(tags=['rooms'])
    def post(self, request):
        serializer = RoomCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        slug = slugify(data['name'])
        exists = Room.objects.filter(slug=slug).exists()
        if exists:
            return ErrorResponse(status=status.HTTP_409_CONFLICT, error='name-taken')
        cube = Cube.objects.get(identifier=data['cube'])
        room = Room(name=data['name'], description=data['description'], slug=slug, password=data['password'], cube=cube)
        room.save()
        room.notify_update()

        start_new_turn(room)

        read_serializer = RoomsReadSerializer(room)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(tags=['rooms'])
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomsReadSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomView(APIView):

    @swagger_auto_schema(tags=['rooms'])
    def get(self, request, room_slug):
        room = get_object_or_404(Room, slug=room_slug)
        serializer = RoomReadSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
