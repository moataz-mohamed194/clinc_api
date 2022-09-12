from django.urls import path

from users.views import GetClinicData, GetAllRequestedAddedByUser, AddAccount, Login

app_name = 'users'
urlpatterns = [
    path('get_clinic_data/', GetClinicData.as_view(), name='get_clinic_data'),
    path('get_all_booking_requisted/', GetAllRequestedAddedByUser.as_view(), name='get_all_booking_requisted'),
    path('add_account/', AddAccount.as_view(), name='add_account'),
    path('login/', Login.as_view(), name='login')

]
