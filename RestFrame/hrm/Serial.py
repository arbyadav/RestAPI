from rest_framework import serializers
from hrm.models import UsersD

class UsersDSerial(serializers.ModelSerializer):
    name=serializers.CharField(required=False)
    employee_id=serializers.CharField(required=False)
    ranking= serializers.FloatField(required=False)

    class Meta:
        model=UsersD
        fields='__all__'