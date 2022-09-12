from rest_framework import serializers
from nurse.models import Visitor, Row


class VisitorSerializers(serializers.ModelSerializer):
    added_by_name = serializers.CharField(source="added_by.name", required=False)

    class Meta:
        model = Visitor
        fields = "__all__"


class SickSerializers(serializers.ModelSerializer):
    approved_by_name = serializers.CharField(source="approved_by.name", required=False)
    added_by_name = serializers.CharField(source="added_by.username", required=False)

    class Meta:
        model = Row
        fields = "__all__"
