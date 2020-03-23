from django.db.models import Q
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    API endpoint that allows transactions to be viewed.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, format=None):
        queryset = Transaction.objects.filter(
            Q(from_user=request.user) | Q(to_user=request.user)
        )
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
