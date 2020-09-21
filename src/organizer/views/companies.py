from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
)

from ..models import Company
from ..serializers import CompanySerializer


class CompanyApiDetail(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "slug"


class CompanyApiList(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

