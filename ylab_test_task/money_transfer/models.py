from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField

from ylab_test_task.users.models import User


class Transaction(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('From user'),
        related_name='transactions_out'
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('To user'),
        related_name='transactions_in'
    )
    amount = MoneyField(
        verbose_name=_('Amount of money sent'),
        max_digits=14,
        decimal_places=2,
        default_currency='USD'
    )