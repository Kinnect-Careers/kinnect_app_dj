from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from ..models import Partner
from ..serializers import PartnerSerializer


class PartnerApiDetail(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = "slug"


class PartnerApiList(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

