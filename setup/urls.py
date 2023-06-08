from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from escola import views
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'
ROUTER = NestedDefaultRouter()
STUDENTS = ROUTER.register('students', views.StudentViewSet, basename='Students')
COURSE = ROUTER.register('courses', views.CourseViewSet, basename='Courses')
ENROLMENT = ROUTER.register('enrolments', views.EnrolmentViewSet, basename='Enrolment')
STUDENTS.register(
    'enrolments',
    views.ListStudentEnrolmentViewSet,
    basename='students-enrolments',
    parents_query_lookups=['students']
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(ROUTER.urls))
]
