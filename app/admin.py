from app.models import Student, Teacher, Profile, StudentCourse
from django.contrib import admin

from app.models import Course, Term


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'point')
    readonly_fields = ('id',)


admin.site.register(Course, CourseAdmin)


class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    readonly_fields = ('id',)


admin.site.register(Term, TermAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'std_number')
    readonly_fields = ('id',)


admin.site.register(Student, StudentAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'field', 'birth_day', 'last_name', 'first_name')
    readonly_fields = ('id',)


admin.site.register(Profile, ProfileAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'department')
    readonly_fields = ('id',)


admin.site.register(Teacher, TeacherAdmin)

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark')
    readonly_fields = ('id',)

admin.site.register(StudentCourse, StudentCourseAdmin)
