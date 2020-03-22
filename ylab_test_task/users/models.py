from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from djmoney.models.managers import money_manager
from djmoney.money import Money


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given  email, password, and balance.
        """
        email = self.normalize_email(email)
        if not email:
            raise ValueError('Valid email is required to create a user')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    balance = MoneyField(
        verbose_name=_('balance'),
        max_digits=14,
        decimal_places=2,
        default=Money(0, 'USD'),
        default_currency='USD'
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = money_manager(UserManager())

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission.
        """
        # Active superusers have all permissions.
        return self.is_superuser
    has_perms = has_perm

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        """
        # Active superusers have all permissions.
        return self.is_superuser
