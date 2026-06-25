from rest_framework import serializers
from .models import Student, lesson, exam, deadline

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = lesson
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = exam
        fields = '__all__'


class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = deadline
        fields = '__all__'

        