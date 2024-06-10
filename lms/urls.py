from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateApiView,
                       LessonDestroyApiView, LessonListApiView,
                       LessonRetrieveApiView, LessonUpdateApiView,
                       SubscriptionAPIView)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("courses", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/delete", LessonDestroyApiView.as_view(), name="lessons_delete"
    ),
    path(
        "lessons/<int:pk>/update", LessonUpdateApiView.as_view(), name="lessons_update"
    ),
    path("course/subscribe/", SubscriptionAPIView.as_view(), name="course_subscribe"),
] + router.urls
