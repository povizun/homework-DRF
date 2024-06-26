from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateApiView,
                       LessonDestroyApiView, LessonListApiView,
                       LessonRetrieveApiView, LessonUpdateApiView,
                       SubscriptionAPIView, SubscriptionCreateAPIView)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("courses", CourseViewSet, basename="courses")

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
    path(
        "courses/subscribe_old/",
        SubscriptionAPIView.as_view(),
        name="course_subscribe_old",
    ),
    path(
        "courses/subscribe/",
        SubscriptionCreateAPIView.as_view(),
        name="course_subscribe",
    ),
] + router.urls
