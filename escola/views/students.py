from rest_framework import viewsets, generics
from escola.models import *
from escola.serializers import *
from rest_framework.viewsets import GenericViewSet

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListStudentEnrolmentViewSet(generics.ListAPIView, GenericViewSet):
    queryset = Enrolment.objects.all()
    serializer_class = StudentEnrolmentSerializer

    def get_queryset(self):
        student = self.kwargs['parent_lookup_students']
        return Enrolment.objects.filter(student=student)

