from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Resume
from ..serializers import ResumeSerializer


class ResumeApiDetail(APIView):
    def get(self, request, slug):
        resume = get_object_or_404(Resume, slug=slug)
        s_resume = ResumeSerializer(
            resume,
            context={"request": request}
        )
        return Response(s_resume.data)


class ResumeApiList(APIView):
    def get(self, request):
        resume_list = get_list_or_404(Resume)
        s_resume = ResumeSerializer(
            resume_list,
            many=True,
            context={"request": request}
        )
        return Response(s_resume.data)
