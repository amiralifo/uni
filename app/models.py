from django.db import models
from django.db.models import (
    Avg,
    Count,
    Max,
    Sum,
)


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_day = models.DateField(blank=True, null=True)
    field = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    std_number = models.IntegerField(null=False, blank=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='Students')

    @property
    def average(self):
        sum_nums = 0
        for item in self.student_courses.all():
            sum_nums = sum_nums + item.mark
        result = sum_nums/self.student_courses.count()
        return result

    @property
    def avg(self):
        return self.student_courses.aggregate(sum_mark=Sum('mark'))['sum_mark']/self.student_courses.count()

    @property
    def avg2(self):
        return self.student_courses.aggregate(avg_mark=Avg('mark'))['avg_mark']


class Teacher(models.Model):
    department = models.CharField(max_length=30)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Term(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    @property
    def course_count(self):
        return self.courses.count()


class Course(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_courses')
    mark = models.FloatField(blank=True, null=True)
