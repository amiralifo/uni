from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    reshte = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    number_std = models.IntegerField(null=False, blank=False)
    profile = models.OneToOneField(Profile)


class Techer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Cours(models.Model):
    name = models.CharField(max_length=30)
    vahed = models.IntegerField()


class Term(models.Model):
    term = models.IntegerField(null=False, blank=False)

