from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons_in_course = SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson')

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_in_course(self, instance):
        return instance.lesson.all().count()
