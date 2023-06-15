from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from escola import views
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
COURSE.register(
    'enrolments',
    views.ListCourseEnrolmentsViewSet,
    basename='courses-enrolments',
    parents_query_lookups=['courses']
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include(ROUTER.urls)),
    path('tokens/', TokenObtainPairView.as_view()),
    path('tokens/refresh', TokenRefreshView.as_view()),
    path('api/v1/auth/', include('rest_framework.urls'))
]
