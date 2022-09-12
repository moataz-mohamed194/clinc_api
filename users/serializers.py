from rest_framework import serializers

from doctor.models import Clinic
from nurse.models import Row
from users.models import *


class ClinicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RowSerializers(serializers.ModelSerializer):
    user_id = serializers.CharField(source="added_by.id", required=False)
    user_username = serializers.CharField(source="added_by.username", required=False)

    class Meta:
        model = Row
        fields = "__all__"
