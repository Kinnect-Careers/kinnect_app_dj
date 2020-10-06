from django.contrib.auth.models import Group, User
from rest_framework import permissions
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
    GroupSerializer,
    UserSerializer,
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

from organizer.viewsets import HasTagViewSet


class UserViewSet(ModelViewSet):
    """ API endpoint that allow users to edit their profile """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(HasTagViewSet):
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


