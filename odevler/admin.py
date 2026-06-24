from django.contrib import admin

from .models import Student,lesson,exam,deadline

admin.site.register(Student)
admin.site.register(lesson)
admin.site.register(exam)
admin.site.register(deadline)
# Register your models here.
