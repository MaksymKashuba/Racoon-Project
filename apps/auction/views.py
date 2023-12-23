from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.auction.models import AuctionsModel
from apps.auction.serializers import AuctionsSerializers


class AuctionsView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = AuctionsModel.objects.all()
    serializer_class = AuctionsSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if 'pk' in self.kwargs:
            queryset = AuctionsModel.objects.filter(lot_id__owner=user)
        else:
            queryset = AuctionsModel.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):

        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)