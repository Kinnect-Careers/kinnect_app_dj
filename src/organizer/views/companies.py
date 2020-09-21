from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from ..models import Company
from ..serializers import CompanySerializer


class CompanyApiDetail(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "slug"


class CompanyApiList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

