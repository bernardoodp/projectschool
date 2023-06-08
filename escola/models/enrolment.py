from django.db import models
from .student import Student
from .course import Course

class Enrolment(models.Model):
    PERIOD = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default='M')
    