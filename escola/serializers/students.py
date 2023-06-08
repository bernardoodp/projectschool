from rest_framework import serializers
from escola.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'name', 'rg', 'cpf', 'born_date',
        ]

class StudentEnrolmentSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Enrolment
        fields = ['courses', 'period']

    def get_courses(self, obj):
        return {
            'id': obj.course.id,
            'code_course': obj.course.code_course,
            'description': obj.course.description,
            'level': obj.course.level
        }