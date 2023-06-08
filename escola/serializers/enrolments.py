from rest_framework import serializers
from escola.models import Enrolment

class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment
        fields = '__all__'