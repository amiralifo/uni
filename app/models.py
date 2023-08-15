from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_day = models.DateField(blank=True, null=True)
    field = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    std_number = models.IntegerField(null=False, blank=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Teacher(models.Model):
    department = models.CharField(max_length=30)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)


class Term(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mark = models.FloatField(blank=True, null=True)
