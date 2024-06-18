import smtplib

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription


@shared_task
def send_mail_about_course_update(course):
    """Отправка письма об обновлении курса подписанным пользователям"""
    subscriptions = Subscription.objects.filter(course=course.pk)
    try:
        send_mail(
            "Курс, на который вы подписаны, обновился",
            f"Курс {course.title} обновился",
            EMAIL_HOST_USER,
            [subscription.user.email for subscription in subscriptions],
        )
    except smtplib.SMTPException as e:
        print(f"Ошибка отправки рассылки: {e}")
