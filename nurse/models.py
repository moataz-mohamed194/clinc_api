import datetime

from django.contrib.auth.models import User
from django.db import models

TYPE_OF_SICK = [
        ("", "--------"),
        ("A", "Consultation"),
        ("B", "Statement"),
    ]


class Nurse (models.Model):
    name = models.CharField('name of visitor', max_length=400)
    first_phone_number = models.IntegerField('first phone number')
    second_phone_number = models.IntegerField('second phone number', blank=True, null=True)
    email = models.EmailField('nurse email', unique=True)
    password = models.CharField('nurse password', max_length=400)
    description = models.TextField('description about nurse')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'nurse'
        verbose_name_plural = 'nurse'


class Visitor (models.Model):
    name = models.CharField('name of visitor', max_length=400)
    reason_of_visitor = models.TextField('reason of visitor')
    added_by = models.ForeignKey(
        Nurse,
        on_delete=models.DO_NOTHING,
        verbose_name='added by',
        related_query_name='visitor_to_doctor',
        related_name='visitor_to_doctor'
    )
    time = models.DateField('date of visit', default=datetime.date.today)
    approved = models.BooleanField('approved by doctor', default=False)
    soft_delete = models.BooleanField('entered', default=False)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} , {self.reason_of_visitor}'

    class Meta:
        verbose_name = 'visitor'
        verbose_name_plural = 'visitor'


class Row(models.Model):
    name = models.TextField('sick name')
    phone_number = models.IntegerField('sick phone number')
    added_by = models.ForeignKey(User, verbose_name='added by', on_delete=models.DO_NOTHING)
    doctor_report = models.TextField('doctor report', blank=True, null=True)
    approved = models.BooleanField('approved by nurse', default=False)
    time = models.DateField('date of Statement', default=datetime.date.today)
    soft_delete = models.BooleanField('entered', default=False)
    type_of_statement = models.CharField(
            max_length=1,
            choices=TYPE_OF_SICK,
            default="",
            verbose_name="type of statement",
        )
    approved_by = models.ForeignKey(
        Nurse,
        on_delete=models.DO_NOTHING,
        verbose_name='approved by',
        related_query_name='approved_by_nurse',
        related_name='approved_by_nurse',
        blank=True,
        null=True
    )
    objects = models.Manager()

    class Meta:
        verbose_name = 'Sick'
        verbose_name_plural = "Sick"

    def __str__(self):
        return self.name
