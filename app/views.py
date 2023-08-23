from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from app.models import Term, Course, Student, StudentCourse
from app.serializers import TermSerializer, CourseInfoSerializer, StudentSerializer, StudentCourseSerializer


class FirstApiView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        return Response('first api')


class TermApiView(ListAPIView):

    def get(self, request, *args, **kwargs):
        terms = Term.objects.all()
        serialized_data = TermSerializer(terms, many=True)
        return Response(serialized_data.data)


class CourseApiView(ListAPIView):

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serialized_data = CourseInfoSerializer(courses, many=True)
        return Response(serialized_data.data)


class StudentApiView(ListAPIView):

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serialized_data = StudentSerializer(students, many=True)
        return Response(serialized_data.data)


class StudentCourseApiView(ListAPIView):

    def get(self, request, *args, **kwargs):
        student_courses = StudentCourse.objects.all()
        serialized_data = StudentCourseSerializer(student_courses, many=True)
        return Response(serialized_data.data)

