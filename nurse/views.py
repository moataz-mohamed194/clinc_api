from django.http import JsonResponse
from rest_framework import generics
from nurse.models import *
from nurse.serializers import VisitorSerializers, SickSerializers


class ApproveBooking(generics.RetrieveUpdateAPIView):
    def patch(self, request, *args, **kwargs):
        data = self.request.data
        try:
            user_data = User.objects.get(id=data['user_pk'])
            approve_row = Row.objects.get(id=data['row_pk'])
            nurse_data = Nurse.objects.get(email=user_data.email)
            approve_row.approved = True
            approve_row.approved_by = nurse_data
            approve_row.save()
            data = {
                'Results': "Success request"
            }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class AddVisitor(generics.ListCreateAPIView):
    serializer_class = VisitorSerializers

    def get_queryset(self):
        date = datetime.date.today()
        data_query = Visitor.objects.filter(time=date).all()
        return data_query

    def post(self, request, *args, **kwargs):
        data = self.request.data
        try:
            user_data = User.objects.get(id=data['pk'])
            nurse_data = Nurse.objects.get(email=user_data.email)
            new_data = Visitor(
                name=data['name'],
                reason_of_visitor=data['reason_of_visitor'],
                approved=False,
                added_by=nurse_data
            )
            new_data.save()
            data = {
                'Results': "Success request"
            }
        except Exception as e:
            data = {
                'Results': f"{e}"
            }
        return JsonResponse(data)


class AddBooking(generics.ListCreateAPIView):
    serializer_class = SickSerializers

    def post(self, request, *args, **kwargs):
        data = self.request.data
        try:
            user_data = User.objects.get(id=data['pk'])
            if Nurse.objects.filter(email=user_data.email).count() > 0:
                nurse_data = Nurse.objects.get(email=user_data.email)
                row_data = Row(
                    name=data['name'],
                    phone_number=data['phone_number'],
                    added_by=user_data,
                    approved=True,
                    type_of_statement=data['type_of_statement'],
                    approved_by=nurse_data
                )
                row_data.save()
            else:
                row_data = Row(
                    name=data['name'],
                    phone_number=data['phone_number'],
                    added_by=user_data,
                    approved=False,
                    type_of_statement=data['type_of_statement'],
                )
                row_data.save()
            data = {
                'Results': "Success request"
            }
        except:
            data = {
                'Results': "Check the login"
            }
        return JsonResponse(data)

    def get_queryset(self):
        date = datetime.date.today()
        data_query = Row.objects.filter(time=date)
        return data_query
