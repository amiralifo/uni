
from rest_framework import serializers

from app.models import Term, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'point']


class TermSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Term
        fields = ['id', 'title', 'courses']


class TermMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ['id', 'title']


class CourseInfoSerializer(serializers.ModelSerializer):
    term = TermMinSerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'point', 'term']