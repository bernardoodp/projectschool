from rest_framework import serializers
from escola.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'name', 'rg', 'cpf', 'born_date',
        ]