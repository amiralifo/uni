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
