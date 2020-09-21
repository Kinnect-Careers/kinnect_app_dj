from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Institution
from ..serializers import InstitutionSerializer


class InstitutionApiDetail(APIView):
    def get(self, request, slug):
        school = get_object_or_404(Institution, slug=slug)
        s_school = InstitutionSerializer(
            school,
            context={"request": request}
        )
        return Response(s_school.data)


class InstitutionApiList(APIView):
    def get(self, request):
        schools_list = get_list_or_404(Institution)
        s_school = InstitutionSerializer(
            schools_list,
            many=True,
            context={"request": request}
        )
        return Response(s_school.data)

