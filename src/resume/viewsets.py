from rest_framework.viewsets import ModelViewSet

from .models import (
    Skill,
    Experience,
    Task,
    Contact,
    Link,
    Institution,
    Education,
    Resume,
    ApplicationSubmission,
)

from .serializers import (
    SkillSerializer,
    ExperienceSerializer,
    TaskSerializer,
    ContactSerializer,
    LinkSerializer,
    InstitutionSerializer,
    EducationSerializer,
    ResumeSerializer,
    ApplicationSubmissionSerializer
)


class SkillViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TaskViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ExperienceViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ContactViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class LinkViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class InstitutionViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class EducationViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ResumeViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class SubmissionViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = ApplicationSubmission.objects.all()
    serializer_class = ApplicationSubmissionSerializer


