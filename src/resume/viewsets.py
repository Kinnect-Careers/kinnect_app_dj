from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    Skill,
    Experience,
    Personal,
    Institution,
    Education,
    Other,
    Resume,
    ApplicationSubmission,
)

from .serializers import (
    GroupSerializer,
    UserSerializer,
    SkillSerializer,
    ExperienceSerializer,
    PersonalSerializer,
    OtherSerializer,
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
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class SkillViewSet(HasTagViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    #permission_classes = [IsAuthenticated]


class ExperienceViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def perform_create(self, serializer):
        serializer.save()

class OtherViewSet(ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer

class PersonalViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        resume = self.get_object()
        serializer = self.get_serializer(resume, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return super().update(request, *args, **kwargs)


class SubmissionViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = ApplicationSubmission.objects.all()
    serializer_class = ApplicationSubmissionSerializer


