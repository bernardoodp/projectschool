from rest_framework import viewsets, generics
from escola.models import *
from escola.serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudentEnrolmentViewSet(generics.ListAPIView, GenericViewSet):
    queryset = Enrolment.objects.all()
    serializer_class = StudentEnrolmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        student = self.kwargs['parent_lookup_students']
        return Enrolment.objects.filter(student=student)

