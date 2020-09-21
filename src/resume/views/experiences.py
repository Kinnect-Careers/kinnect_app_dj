from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from ..models import Experience
from ..serializers import (
    ExperienceSerializer,
    TaskSerializer
)


class ExperienceApiDetail(RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_object(self):
        slug  = self.kwargs.get("slug")
        queryset = self.filter_queryset(self.get_queryset())

        experience = get_object_or_404(
            queryset,
            slug=slug
        )
        self.check_object_permissions(
            self.request, experience
        )
        return experience


class ExperienceApiList(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
