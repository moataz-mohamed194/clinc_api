from decimal import Decimal
import calendar
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics
import datetime
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from doctor.models import Fees, Clinic, Doctor
from doctor.serializers import NurseSerializers, FeesSerializers, DoctorSerializers, ClinicSerializers
from nurse.models import Visitor, Nurse, Row
from nurse.serializers import VisitorSerializers


class ApproveVisitor(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VisitorSerializers

    def patch(self, request, *args, **kwargs):
        data = self.request.data
        try:
            approve_row = Visitor.objects.get(id=data['pk'])
            approve_row.approved = True
            approve_row.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "Check the request"
            }
        return JsonResponse(data)


class AddFees(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            get_data = self.request.data
            print(get_data['price'])
            print(Decimal(get_data['price']))
            add_data = Fees(
                type=get_data['type'],
                price=Decimal(get_data['price']),
                time=get_data['time'],
            )
            add_data.save()
            data = {
                'Results': "Success request"
            }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class FeesUpdateAndDeleteAndGet(RetrieveUpdateDestroyAPIView):
    serializer_class = FeesSerializers
    queryset = Fees.objects.all()

    def get_object(self):
        data = self.request.data
        query_set = self.filter_queryset(self.get_queryset())
        obj = query_set.get(id=data['pk'])
        return obj

    def delete(self, request, *args, **kwargs):
        data = self.request.data
        print(data)
        delete_data = Fees.objects.filter(id=data['pk'])
        delete_data.delete()
        return JsonResponse({
                'Results': "Success request"
            })

    def patch(self, request, *args, **kwargs):
        data = self.request.data
        try:
            fees_data = Fees.objects.get(id=data['pk'])
            fees_data.type = data['type']
            fees_data.price = Decimal(data['price'])
            fees_data.time = data['time']
            fees_data.save()
            data = {
                'Results': "Success request"
            }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class GetFeesOfDay(generics.ListAPIView):
    serializer_class = FeesSerializers

    def get_queryset(self):
        data_query = Fees.objects.filter(time=self.kwargs['date']).all()
        return data_query


class GetFeesOfMonth(generics.ListAPIView):
    serializer_class = FeesSerializers

    def get_queryset(self):
        date_object = datetime.datetime.strptime(self.kwargs['date'], '%Y-%m-%d').date()
        month = date_object.month
        year = date_object.year
        start_month = datetime.date(year, month, 1)
        end_month = datetime.date(year, month, calendar.monthrange(year, month)[1])
        data_query = Fees.objects.filter(time__gte=start_month, time__lte=end_month).all()
        return data_query


class AddNurse(generics.ListCreateAPIView):
    serializer_class = NurseSerializers

    def post(self, request, *args, **kwargs):
        data_sign = self.request.data
        try:
            if User.objects.filter(email=data_sign['email']).count() > 0:
                data = {
                    'Results': "email is used"
                }
                return JsonResponse(data)
            else:
                try:
                    int(data_sign['second_phone_number'])
                    second_phone_number = data_sign['second_phone_number']
                except:
                    second_phone_number = None
                nurse_data = Nurse(
                    name=data_sign['userName'],
                    email=data_sign['email'],
                    password=data_sign['password'],
                    first_phone_number=data_sign['first_phone_number'],
                    second_phone_number=second_phone_number,
                    description=data_sign['description']
                )
                nurse_data.save()
                user = User.objects.create_user(
                    username=data_sign['userName'],
                    email=data_sign['email'],
                    password=data_sign['password'])
                user.save()
                data = {
                    'Results': "Success request"
                }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)

    def get_queryset(self):
        try:
            return Nurse.objects.all()
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
            return JsonResponse(data)


class AddReportForSick(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        data_clean = self.request.data
        try:
            update_data = Row.objects.get(id=data_clean['pk'])
            update_data.doctor_report = data_clean['doctor_report']
            update_data.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "check your data again"
            }
        return JsonResponse(data)


class EditDataClinic(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        data_clean = self.request.data
        try:
            update_data = Clinic.objects.get(id=data_clean['pk'])
            update_data.address = data_clean['address']
            update_data.note = data_clean['note']
            update_data.from_time = data_clean['from_time']
            update_data.to_time = data_clean['to_time']
            update_data.time_of_vacation = data_clean['time_of_vacation']
            update_data.latitude = data_clean['latitude']
            update_data.longitude = data_clean['longitude']
            update_data.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "check your data again"
            }
        return JsonResponse(data)


class EditDataDoctor(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        data_clean = self.request.data
        try:
            update_data = Doctor.objects.get(id=data_clean['pk'])
            update_data.name = data_clean['name']
            update_data.phone_number = data_clean['phone_number']
            update_data.email = data_clean['email']
            update_data.password = data_clean['password']
            update_data.description = data_clean['description']
            update_data.pic = data_clean['pic']
            update_data.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "check your data again"
            }
        return JsonResponse(data)


class ModelOfClinic(generics.ListCreateAPIView):
    serializer_class = ClinicSerializers

    def get_queryset(self):
        try:
            return Clinic.objects.all()
        except:
            data = {
                'Results': "check your data again"
            }
            return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data_clean = self.request.data
        try:
            new_data = Clinic(
                address=data_clean['address'],
                note=data_clean['note'],
                from_time=data_clean['from_time'],
                to_time=data_clean['to_time'],
                time_of_vacation=data_clean['time_of_vacation'],
                longitude=data_clean['longitude'],
                latitude=data_clean['latitude']
            )
            new_data.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "check your data again"
            }
        return JsonResponse(data)


class ModelOfDoctor(generics.ListCreateAPIView):
    serializer_class = DoctorSerializers

    def get_queryset(self):
        try:
            return Doctor.objects.all()
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
            return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data_clean = self.request.data
        try:
            if User.objects.filter(email=data_clean['email']).count() > 0:
                data = {
                    'Results': "email is used"
                }
                return JsonResponse(data)
            else:
                user = User.objects.create_user(
                    username=data_clean['name'],
                    email=data_clean['email'],
                    password=data_clean['password'])
                new_data = Doctor(
                    name=data_clean['name'],
                    phone_number=data_clean['phone_number'],
                    email=data_clean['email'],
                    password=data_clean['password'],
                    description=data_clean['description'],
                    pic=data_clean['pic'],
                )
                new_data.save()
                user.save()

                data = {
                    'Results': "Success request"
                }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class ClinicGetAndDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ClinicSerializers
    queryset = Clinic.objects.all()

    def get_object(self):
        data = self.request.data
        query_set = self.filter_queryset(self.get_queryset())
        obj = query_set.get(id=data['pk'])
        return obj

    def delete(self, request, *args, **kwargs):
        data = self.request.data
        print(data)
        delete_data = Clinic.objects.filter(id=data['pk'])
        delete_data.delete()
        return JsonResponse({
                'Results': "Success request"
            })


class DoctorGetAndDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializers
    queryset = Doctor.objects.all()

    def get_object(self):
        data = self.request.data
        query_set = self.filter_queryset(self.get_queryset())
        obj = query_set.get(id=data['pk'])
        return obj

    def delete(self, request, *args, **kwargs):
        data = self.request.data
        print(data)
        delete_data = Doctor.objects.filter(id=data['pk'])
        delete_data.delete()
        return JsonResponse({
                'Results': "Success request"
            })
