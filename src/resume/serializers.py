from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
)
from .models import (
    Skill,
    Experience,
    Task,
    Institution,
    Education,
    Contact,
    Link,
    Resume,
    ApplicationSubmission,
)

import sys
sys.path.append('..')
from organizer.models import Company
from organizer.serializers import TagSerializer, CompanySerializer, JobSerializer


class SkillSerializer(HyperlinkedModelSerializer):
    """Serializer for Skill data"""
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        #exclude = ("id",)
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-skill-detail",
            }
        }


class TaskSerializer(ModelSerializer):
    """Serializer for Task data"""

    class Meta:
        model = Task
        exclude = ("id", "experience")


class ExperienceSerializer(ModelSerializer):
    """Serializer for Experience data"""
    company = HyperlinkedRelatedField(
        queryset=Company.objects.all(),
        lookup_field="slug",
        view_name="api-company-detail",
    )
    task_set = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Experience
        #fields = "__all__"
        exclude = ("id",)


class InstitutionSerializer(HyperlinkedModelSerializer):
    """Serializer for Institutions data"""
    class Meta:
        model = Institution
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-institution-detail",
            }
        }


class EducationSerializer(ModelSerializer):
    """Serializer for Education data"""
    institution = HyperlinkedRelatedField(
        queryset=Institution.objects.all(),
        lookup_field="slug",
        view_name="api-institution-detail",
    )
    class Meta:
        model = Education
        exclude = ("id",)


class ContactSerializer(HyperlinkedModelSerializer):
    """Serializer for Contacts data"""
    class Meta:
        model = Contact
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-contact-detail",
            }
        }


class LinkSerializer(HyperlinkedModelSerializer):
    """Serializer for Links data"""
    class Meta:
        model = Link
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-link-detail",
            }
        }


class ResumeSerializer(ModelSerializer):
    """Serializer for Resume data"""
    contacts = ContactSerializer(many=True, read_only=True)
    links = LinkSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        exclude = ("id",)


class ApplicationSubmissionSerializer(ModelSerializer):
    """Serializer for Application Submission data"""
    resume = ResumeSerializer
    job = JobSerializer
    class Meta:
        model = ApplicationSubmission
        fields = "__all__"

