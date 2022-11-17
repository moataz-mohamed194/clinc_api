from django.urls import path

from doctor.views import *

app_name = 'doctor'

urlpatterns = [
    path('approve_visitor/', ApproveVisitor.as_view(), name='approve_visitor'),
    path('add_fees/', AddFees.as_view(), name='add_fees'),
    path('fees_update_delete_get/', FeesUpdateAndDeleteAndGet.as_view(), name='fees_update_delete_get'),
    path('get_fees_of_day/<str:date>', GetFeesOfDay.as_view(), name='get_fees_of_day'),
    path('get_fees_of_month/<str:date>', GetFeesOfMonth.as_view(), name='get_fees_of_month'),
    path('add_nurse/', AddNurse.as_view(), name='add_nurse'),
    path('add_report_for_sick/', AddReportForSick.as_view(), name='add_report_for_sick'),
    path('edit_data_clinic/', EditDataClinic.as_view(), name='edit_data_clinic'),
    path('edit_data_doctor/', EditDataDoctor.as_view(), name='edit_data_doctor'),
    path('model_of_clinic/', ModelOfClinic.as_view(), name='model_of_clinic'),
    path('model_of_doctor/', ModelOfDoctor.as_view(), name='model_of_doctor'),
    path('clinic_get_delete/', ClinicGetAndDelete.as_view(), name='clinic_get_delete'),
    path('doctor_get_delete/', DoctorGetAndDelete.as_view(), name='doctor_get_delete'),

]
