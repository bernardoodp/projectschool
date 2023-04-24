from django.db import models

class Course(models.Model):
    NIVEL= (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    code_course = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL)

    def __str__(self):
        return self.code_course