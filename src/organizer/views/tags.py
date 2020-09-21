from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from ..serializers import TagSerializer
from ..models import Tag


class TagApiDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagApiList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

