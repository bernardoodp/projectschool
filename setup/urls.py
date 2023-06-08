from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from escola.views import StudentViewSet, CourseViewSet, EnrolmentViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('enrolments', EnrolmentViewSet, basename='Enrolment')
urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
