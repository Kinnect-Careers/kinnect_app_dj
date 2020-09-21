from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer
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
from organizer.serializers import TagSerializer, CompanySerializer, JobSerializer


class SkillSerializer(HyperlinkedModelSerializer):
    """Serializer for Skill data"""
    tags = TagSerializer(many=True)

    class Meta:
        model = Skill
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
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    """Serializer for Experience data"""
    #task_set = TaskSerializer(many=True)
    company = CompanySerializer
    task_set = TaskSerializer(many=True)
    class Meta:
        model = Experience
        fields = "__all__"


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
    institution = InstitutionSerializer
    class Meta:
        model = Education
        fields = "__all__"


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
    contacts = ContactSerializer(many=True)
    links = LinkSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    educations = EducationSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = Resume
        fields = "__all__"


class ApplicationSubmissionSerializer(ModelSerializer):
    """Serializer for Application Submission data"""
    resume = ResumeSerializer
    job = JobSerializer
    class Meta:
        model = ApplicationSubmission
        fields = "__all__"

