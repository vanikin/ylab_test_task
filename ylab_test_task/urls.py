from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .money_transfer import views as transactions_views
from .users import views as users_views

router = routers.DefaultRouter()
router.register(r'transactions', transactions_views.TransactionViewSet)
router.register(r'users', users_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
