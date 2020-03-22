from django.contrib import admin
from django.contrib.auth import (
    models as auth_models,
    admin as auth_admin
)
from django.utils.translation import gettext, gettext_lazy as _

from . import models


admin.site.unregister(auth_models.Group)


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'balance')}),
        (_('Permissions'), {'fields': ('is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', )}),
    )
    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser', )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()