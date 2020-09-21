from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView
)

from ..models import Job
from ..serializers import JobSerializer

class JobApiDetail(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    def get_object(self):
        partner_slug = self.kwargs.get("partner_slug")
        job_slug = self.kwargs.get("job_slug")

        queryset = self.filter_queryset(self.get_queryset())
        job = get_object_or_404(
            queryset,
            slug=job_slug,
            partner__slug=partner_slug,
        )
        self.check_object_permissions(
            self.request, job
        )
        return job

class JobApiList(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

