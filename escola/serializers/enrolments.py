from rest_framework import serializers
from escola.models import Enrolment
from escola.serializers import StudentSerializer, CourseSerializer

class EnrolmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()
    class Meta:
        model = Enrolment
        fields = ['id','student', 'course', 'period']