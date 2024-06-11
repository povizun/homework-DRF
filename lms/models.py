from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Навзвание", help_text="Укажите название курса"
    )
    preview_image = models.ImageField(
        upload_to="lms/course/preview",
        **NULLABLE,
        verbose_name="превью изображение",
        help_text="Загрузите ваше превью курса",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Введите описание курса"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="владелец",
        help_text="Укажите владельца",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Навзвание", help_text="Укажите название урока"
    )
    preview_image = models.ImageField(
        upload_to="lms/lesson/preview",
        **NULLABLE,
        verbose_name="превью изображение",
        help_text="Загрузите ваше превью урока",
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Введите описание урока"
    )
    video_link = models.CharField(
        max_length=100,
        verbose_name="ссылка на видео",
        help_text="Укажите ссылку на видео",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
        related_name="lesson",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="владелец",
        help_text="Укажите владельца",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="пользователь",
        help_text="Укажите пользователя",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс в подписке",
        help_text="Укажите курс",
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
