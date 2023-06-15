from rest_framework import viewsets
from escola.models import Enrolment
from escola.serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateEnrolmentSerializer
        else:
             return EnrolmentSerializer