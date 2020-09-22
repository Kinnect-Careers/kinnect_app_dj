from rest_framework.viewsets import ModelViewSet

from .models import (
    Tag,
    Company,
    Partner,
    Job,
)

from .serializers import (
    TagSerializer,
    CompanySerializer,
    PartnerSerializer,
    JobSerializer,
)


class TagViewSet(ModelViewSet):
    """ Views for Tag """
    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CompanyViewSet(ModelViewSet):
    """ Views for Company """
    lookup_field = "slug"
    queryset = Partner.objects.all()
    serializer_class = CompanySerializer


class PartnerViewSet(ModelViewSet):
    """ Views for Partner """
    lookup_field = "slug"
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class JobViewSet(ModelViewSet):
    """ Views for Job """
    lookup_field = "slug"
    queryset = Job.objects.all()
    serializer_class = JobSerializer

