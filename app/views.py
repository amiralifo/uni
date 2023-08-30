from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from app.models import Term, Course, Student, StudentCourse
from app.serializers import TermSerializer, CourseInfoSerializer, StudentSerializer, StudentCourseSerializer, CreateTermSerializer, CreateCourseSerializer, CreateStudentSerializer
from rest_framework import status


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

class CreateTermAPIView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer = CreateTermSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        term = Term.objects.create(title=serializer.validated_data["title"])
        serializer = CreateTermSerializer(term)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateCourseAPIView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer = CreateCourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.create(name=serializer.validated_data["name"], point=serializer.validated_data["point"],term=serializer.validated_data["term"],)
        serializer = CreateCourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateStudentAPIView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer = CreateStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)