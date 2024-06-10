from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_video_link


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[validate_video_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["title", "description"]


class CourseSerializer(serializers.ModelSerializer):
    lessons_in_course = serializers.SerializerMethodField()
    lessons = LessonCourseSerializer(many=True, source="lesson", read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_in_course(self, instance):
        return instance.lesson.all().count()
