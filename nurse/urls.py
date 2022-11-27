from django.urls import path
from nurse.views import *

app_name = 'nurse'
urlpatterns = [
    path('approve_booking/', ApproveBooking.as_view(), name='approve_booking'),
    path('add_visitor/', AddVisitor.as_view(), name='add_visitor'),
    path('add_booking/', AddBooking.as_view(), name='add_booking'),
    path('entered_sick/<int:pk>/', EnteredSick.as_view(), name='get_booking_sick'),
    path('entered_visited/<int:pk>/', EnteredVisited.as_view(), name='get_booking_sick'),
    # path('get_visitor/', GetVisitor.as_view(), name='get_visitor'),

]
