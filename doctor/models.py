from django.db import models
from os import path
import datetime


def update_pic_filename(instance, original_file_name):
    extension = original_file_name.split('.')[-1]
    new_name = str(instance.id)

    # Search in the Directory for the same number and print error message if found
    filename = 'doctor_pic/{0}.{1}'.format(new_name, extension)
    return path.join('', filename)


class Clinic(models.Model):
    address = models.TextField('address')
    note = models.TextField('note')
    from_time = models.TimeField('when open')
    to_time = models.TimeField('when close')
    time_of_vacation = models.TextField('time of vacation')
    objects = models.Manager()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'clinic data'
        verbose_name_plural = 'clinic data'


class Doctor (models.Model):
    name = models.TextField('name of doctor')
    phone_number = models.IntegerField('doctor phone number')
    email = models.EmailField('doctor email', unique=True)
    password = models.CharField('doctor password', max_length=400)
    description = models.TextField('doctor description')
    pic = models.FileField(
        upload_to=update_pic_filename,
        blank=True, null=True, verbose_name='صورة'

    )
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor data'
        verbose_name_plural = 'Doctor data'


class Fees(models.Model):
    type = models.CharField('type of fees', max_length=400)
    price = models.DecimalField('price fees', max_digits=7, decimal_places=3)
    time = models.DateField('time of fees', default=datetime.date.today)
    objects = models.Manager()

    class Meta:
        verbose_name = 'details of fees'
        verbose_name_plural = 'details of fees'

    def __str__(self):
        return f'{self.type} , {self.price}'
