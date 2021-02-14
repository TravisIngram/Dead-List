from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from deadlist.models import User, Pun, Call, Deceased
from .serializers import UserSerializer, PunSerializer, CallSerializer, DeceasedSerializer


# User routes, Get / Update / Delete a specific user...


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all users in DB or create / add a new one


class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Pun routes, Get / Update / Delete a specific pun...


class PunDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pun = self.get_object(pk)
        serializer = PunSerializer(pun)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pun = self.get_object(pk)
        serializer = PunSerializer(pun, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pun = self.get_object(pk)
        pun.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all puns in DB or create / add a new one


class PunList(APIView):

    def get(self, request, format=None):
        puns = Pun.objects.all()
        serializer = PunSerializer(puns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Call routes, Get / Update / Delete a specific call...


class CallDetail(APIView):

    def get_object(self, pk):
        try:
            return Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        call = self.get_object(pk)
        serializer = CallSerializer(call)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        call = self.get_object(pk)
        serializer = CallSerializer(call, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        call = self.get_object(pk)
        call.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all calls in DB or create / add a new one


class CallList(APIView):

    def get(self, request, format=None):
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deceased routes, Get / Update / Delete a specific deceased person...


class DeceasedDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deceased = self.get_object(pk)
        serializer = DeceasedSerializer(deceased)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deceased = self.get_object(pk)
        serializer = DeceasedSerializer(deceased, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deceased = self.get_object(pk)
        deceased.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all users in DB or create / add a new one


class DeceasedList(APIView):

    def get(self, request, format=None):
        deceased = Deceased.objects.all()
        serializer = DeceasedSerializer(deceased, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeceasedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
