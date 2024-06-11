from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@sky.shop")
        self.course = Course.objects.create(
            title="Test", description="1 course", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Test 1",
            description="1 lesson",
            video_link="https://youtu.be/dQw4w9WgXcQ?si=wkagcOxy3-75pvcs",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "title": "Test_2",
            "video_link": "https://youtu.be/SUiMr3h50_g?si=xrLahAfstNuMuS7x",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.filter(title="Test_2").count(), 1)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {"title": "Test_2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test_2")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_list_lesson(self):
        course = Course.objects.create(
            title="Тестовый курс", description="Тест", owner=self.user
        )

        Lesson.objects.create(
            title="Тестовый урок",
            description="Тест",
            video_link="https://youtu.be/SUiMr3h50_g?si=xrLahAfstNuMuS7x",
            course=course,
            owner=self.user,
        )

        response = self.client.get("/lms/lessons/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@sky.shop")
        self.course = Course.objects.create(
            title="Test", description="1 course", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Test 1",
            description="1 lesson",
            video_link="https://youtu.be/dQw4w9WgXcQ?si=wkagcOxy3-75pvcs",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lms:courses-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_create(self):
        url = reverse("lms:courses-list")
        data = {"title": "Test course 2"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse("lms:courses-detail", args=(self.course.pk,))
        data = {"title": "Test course"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test course")

    def test_course_delete(self):
        url = reverse("lms:courses-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_list_course(self):
        response = self.client.get(
            "/lms/courses/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.course.pk,
                        "lessons_in_course": 1,
                        "is_subscribed": False,
                        "lessons": [
                            {
                                "title": "Test 1",
                                "description": "1 lesson",
                            }
                        ],
                        "title": "Test",
                        "preview_image": None,
                        "description": "1 course",
                        "owner": self.user.pk,
                    }
                ],
            },
        )

    def test_list_course_subscription(self):
        url = reverse("lms:course_subscribe")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(
            "/lms/courses/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.course.pk,
                        "lessons_in_course": 1,
                        "is_subscribed": True,
                        "lessons": [
                            {
                                "title": "Test 1",
                                "description": "1 lesson",
                            }
                        ],
                        "title": "Test",
                        "preview_image": None,
                        "description": "1 course",
                        "owner": self.user.pk,
                    }
                ],
            },
        )
