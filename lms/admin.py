from django.contrib import admin

from lms.models import Course, Lesson, Subscription


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
