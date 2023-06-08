from rest_framework import serializers
from escola.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'name', 'rg', 'cpf', 'born_date',
        ]

class StudentEnrolmentSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrolment
        fields = ['id','courses', 'period']

    def get_period(self,obj):
        return obj.get_period_display()