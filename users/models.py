from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from lms.models import Lesson, Course

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Введите почту"
    )

    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="номер телефона",
        help_text="Укажите ваш номер"
    )
    city = models.CharField(
        max_length=35, **NULLABLE, verbose_name="город", help_text="Укажите ваш город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        **NULLABLE,
        verbose_name="аватар",
        help_text="Загрузите ваш аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'Наличными', _('Наличными')
        CARD = 'Картой', _('Картой')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', help_text='Укажите пользователя', related_name='payment')

    date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты', help_text='Укажите дату оплаты')

    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT, **NULLABLE, verbose_name='урок', help_text='Укажите урок', related_name='payment')
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, **NULLABLE, verbose_name='курс', help_text='Укажите курс', related_name='payment')

    summ = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='оплаченная сумма', help_text='Укажите оплаченную сумму')
    payment_method = models.CharField(verbose_name='Способ оплаты', help_text='Выберите способ оплаты', choices=PaymentMethod)

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
