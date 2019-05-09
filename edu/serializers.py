from .models import Student, Teacher
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()


class CourseSerializer(serializers.Serializer):
    name = serializers.CharField()
    unit = serializers.IntegerField()

class StudentSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    last_modified_date = serializers.DateTimeField()
    user = UserSerializer()
    courses = CourseSerializer(many=True)

    def create(self, validated_data):
        student_data = {}
        student_data['student_id'] = validated_data.pop('student_id')
        student_data['last_modified_date'] = validated_data.pop('last_modified_date')
        user = User.objects.create(**validated_data)
        return Student.objects.create(user=user, **student_data)
