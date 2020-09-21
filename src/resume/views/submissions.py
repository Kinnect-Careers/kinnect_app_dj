from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import ApplicationSubmission
from ..serializers import ApplicationSubmissionSerializer


class ApplicationSubmissionApiDetail(APIView):
    def get(self, request, slug):
        app_submission = get_object_or_404(
            ApplicationSubmission, slug=slug
        )
        s_submission = ApplicationSubmissionSerializer(
            app_submission,
            context={"request": request}
        )
        return Response(s_submission.data)


class ApplicationSubmissionApiList(APIView):
    def get(self, request):
        app_submission_list = get_list_or_404(
            ApplicationSubmission
        )
        s_submission = ApplicationSubmissionSerializer(
            app_submission_list,
            many=True,
            context={"request": request}
        )
        return Response(s_submission.data)
