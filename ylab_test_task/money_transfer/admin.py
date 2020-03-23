from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class UserAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'amount', 'date')
    list_filter = ('amount_currency', )