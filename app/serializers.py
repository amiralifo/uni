
from rest_framework import serializers

from app.models import Term, Course, Profile, Student, StudentCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'point']


class TermSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Term
        fields = ['id', 'title', 'courses', 'course_count']


class TermMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ['id', 'title']


class CourseInfoSerializer(serializers.ModelSerializer):
    term = TermMinSerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'point', 'term']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'field']


class StudentCourseSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = StudentCourse
        fields = ['id', 'mark', 'course']


class StudentSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()
    student_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'std_number', 'profile', 'student_courses', 'average', 'avg', 'avg2']
