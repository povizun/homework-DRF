from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Навзвание", help_text="Укажите название курса"
    )
    preview_image = models.ImageField(
        upload_to="lms/course/preview",
        **NULLABLE,
        verbose_name="превью изображение",
        help_text="Загрузите ваше превью курса"
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Введите описание курса"
    )

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
        help_text="Загрузите ваше превью урока"
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
        on_delete=models.RESTRICT,
        verbose_name="Курс",
        help_text="Выберите курс",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
