from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    Skill,
    Experience,
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
        print(serializer.is_valid())
        print(serializer.validated_data)
        serializer.save()


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("Serializer {}".format(serializer.is_valid()))
        print(serializer.validated_data)
        print("Request")
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        print(len(request.data['educations']))
        #print(len(request.data['links']))
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        resume = self.get_object()
        serializer = self.get_serializer(resume, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        print("Serializer valid {}".format(serializer.is_valid()))
        print(len(serializer.data['educations']))
        return super().update(request, *args, **kwargs)


class SubmissionViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = ApplicationSubmission.objects.all()
    serializer_class = ApplicationSubmissionSerializer


