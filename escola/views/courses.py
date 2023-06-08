from rest_framework import viewsets, generics
from escola.models import Course, Enrolment
from escola.serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListCourseEnrolmentsViewSet(generics.ListAPIView, GenericViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseEnrolmentSerializer

    def get_queryset(self):
        course = self.kwargs['parent_lookup_courses']
        return Enrolment.objects.filter(course=course)