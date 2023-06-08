from rest_framework import viewsets
from escola.models import Enrolment
from escola.serializers import EnrolmentSerializer

class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer