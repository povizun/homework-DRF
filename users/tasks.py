from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import User


@shared_task
def block_inactive_users():
    """Блокирует пользователей, которые не заходили больше месяца"""
    today = timezone.now().date()
    inactive_users = User.objects.filter(
        is_active=True,
        is_staff=False,
        is_superuser=False,
        last_login__lt=(today - relativedelta(months=1)),
    )
    for user in inactive_users:
        user.is_active = False
        user.save()
