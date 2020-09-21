from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Link
from ..serializers import LinkSerializer


class LinkApiDetail(APIView):
    def get(self, request, slug):
        link = get_object_or_404(Link, slug=slug)
        s_link = LinkSerializer(
            link,
            context={"request": request}
        )
        return Response(s_link.data)


class LinkApiList(APIView):
    def get(self, request):
        links_list = get_list_or_404(Link)
        s_link = LinkSerializer(
            links_list,
            many=True,
            context={"request": request}
        )
        return Response(s_link.data)

