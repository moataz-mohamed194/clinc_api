from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics

from doctor.models import *
from nurse.models import Row
from users.models import User
from django.contrib.auth.models import User as MainUser

from users.serializers import ClinicSerializers, UserSerializers, RowSerializers


class GetClinicData(generics.ListCreateAPIView):
    serializer_class = ClinicSerializers
    queryset = Clinic.objects.all()


class AddAccount(generics.CreateAPIView):
    serializer_class = UserSerializers

    def post(self, request, *args, **kwargs):
        data_sign = self.request.data
        try:
            if User.objects.get(email=data_sign['email']).exists():
                data = {
                    'Results': "email is used"
                }
                return JsonResponse(data)
            elif User.objects.get(username=data_sign['userName']).exists():
                data = {
                    'Results': "user name is used"
                }
                return JsonResponse(data)
            else:
                user = User(
                    username=data_sign['userName'],
                    email=data_sign['email'],
                    password=data_sign['password'])
                user.save()
                main_user = MainUser.objects.create_user(
                    username=data_sign['userName'],
                    email=data_sign['email'],
                    password=data_sign['password'])
                main_user.save()
                data = {
                    'Results': "Success request"
                }
        except:
            data = {
                'Results': f"Check your data"
            }
        return JsonResponse(data)


class GetAllRequestedAddedByUser(generics.ListAPIView):
    serializer_class = RowSerializers

    def get_queryset(self):
        return Row.objects.filter(added_by=self.request.data['pk']).all()


class Login(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        data_sign = self.request.data
        print(data_sign)
        username = MainUser.objects.get(email=data_sign['email']).username
        user = authenticate(request,
                            username=username,
                            password=data_sign['password'])

        if user is not None:
            login(request, user)
            if user.is_active:
                data = {'Results': "Success request"}
            else:
                data = {'Results': "False"}
        else:
            data = {'Results': "False0"}

        return JsonResponse(data)