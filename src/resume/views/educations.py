from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Education
from ..serializers import EducationSerializer


class EducationApiDetail(APIView):
    def get(self, request, slug):
        ed = get_object_or_404(Education, slug=slug)
        s_education = EducationSerializer(
            ed,
            context={"request": request}
        )
        return Response(s_education.data)


class EducationApiList(APIView):
    def get(self, request):
        ed_list = get_list_or_404(Education)
        s_education = EducationSerializer(
            ed_list,
            many=True,
            context={"request": request},
        )
        return Response(s_education.data)
