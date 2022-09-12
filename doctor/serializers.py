from rest_framework import serializers

from doctor.models import Clinic, Fees, Doctor
from nurse.models import Nurse


class NurseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"


class FeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = "__all__"


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class ClinicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"
