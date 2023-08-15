from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from app.models import Term, Course
from app.serializers import TermSerializer, CourseSerializer, CourseInfoSerializer


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
