from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)

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


class HasTagViewSet(ModelViewSet):
    """ Base for viewsets with Tags """
    lookup_field = "slug"

    @action(detail=True, methods=["HEAD", "GET", "POST"])
    def tags(self, request, slug=None):
        """ Relate posted tag to tagged object in URI """
        tagged_object = self.get_object()
        if request.method in ("HEAD", "GET"):
            s_tag = TagSerializer(
                tagged_object.tags,
                many=True,
                context={"request": request},
            )
            return Response(s_tag.data)
        tag_slug = request.data.get("slug")
        if not tag_slug:
            return Response(
                "Slug for tag must be specified",
                status=HTTP_400_BAD_REQUEST,
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        tagged_object.tags.add(tag)
        return Response(status=HTTP_204_NO_CONTENT)


class CompanyViewSet(HasTagViewSet):
    """ Views for Company """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PartnerViewSet(HasTagViewSet):
    """ Views for Partner """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class JobViewSet(HasTagViewSet):
    """ Views for Job """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
