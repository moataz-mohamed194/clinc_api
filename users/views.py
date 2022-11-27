from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics

from doctor.models import *
from nurse.models import Row, Nurse
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
            if User.objects.filter(email=data_sign['email']).exists():
                data = {
                    'Results': "email is used"
                }
                return JsonResponse(data)
            if User.objects.filter(username=data_sign['userName']).exists():
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
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class UpdateAccount(generics.ListCreateAPIView):
    serializer_class = UserSerializers

    def post(self, request, *args, **kwargs):
        data_sign = self.request.data

        try:
            main_user_data = MainUser.objects.get(id=self.kwargs['pk'])
            main_user_email = main_user_data.email
            user_data = User.objects.get(email=main_user_email)
            if data_sign['userName']:
                main_user_data.username = data_sign['userName']
                user_data.username = data_sign['userName']
                main_user_data.save()
                user_data.save()
            if data_sign['email']:
                main_user_data.email = data_sign['email']
                user_data.email = data_sign['email']
                main_user_data.save()
                user_data.save()
            data = {
                'Results': "Success request"
            }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class GetAllRequestedAddedByUser(generics.ListAPIView):
    serializer_class = RowSerializers

    def get_queryset(self):
        return Row.objects.filter(added_by=self.kwargs['pk']).all()


class Login(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        data_sign = self.request.data
        print(data_sign)
        username = MainUser.objects.get(email=data_sign['email']).username
        pk = MainUser.objects.get(email=data_sign['email']).id
        user = authenticate(request,
                            username=username,
                            password=data_sign['password'])
        email = data_sign['email']
        if user is not None:
            login(request, user)
            if user.is_active:

                try:
                    nurse = Nurse.objects.get(email=user.email)
                    data = {
                            'Results': "Success request",
                            'pk': user.pk,
                            'name': nurse.name,
                            'typeOfAccount': 'Nurse'
                    }
                except:

                    try:
                        userAccount = User.objects.get(email=user.email)
                        data = {
                            'Results': "Success request",
                            'pk': user.pk,
                            'name': userAccount.username,
                            'typeOfAccount': 'User'
                        }
                    except:
                        try:
                            doctor = Doctor.objects.get(email=user.email)

                            data = {
                                'Results': "Success request",
                                'pk': user.pk,
                                'name': doctor.name,
                                'typeOfAccount': 'Doctor'
                            }
                        except:
                            data = {'Results': "False"}
            else:
                data = {'Results': "False"}
        else:
            data = {'Results': "False0"}

        return JsonResponse(data)
