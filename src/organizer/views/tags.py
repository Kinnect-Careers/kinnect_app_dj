from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
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

    def post(self, request):
        """ Create a new Tag using POST """
        s_tag = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(
                s_tag.data,
                HTTP_201_CREATED
            )
        return Response(
            s_tag.errors,
            HTTP_400_BAD_REQUEST
        )


