from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)
from .models import Tag, Company, Partner, Job
#from resume.serializers import SkillSerializer

class TagSerializer(HyperlinkedModelSerializer):
    """Serializer for Tag data"""
    #skill_set = SkillSerializer(many=True)
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }


class CompanySerializer(HyperlinkedModelSerializer):
    """Serializer for Company data"""
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-company-detail",
            }
        }


class PartnerSerializer(HyperlinkedModelSerializer):
    """Serializer for Partner data"""
    #job_set = JobSerializer(many=True)
    class Meta:
        model = Partner
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-partner-detail",
            }
        }


class JobSerializer(HyperlinkedModelSerializer):
    """Serializer for Job data"""
    partner = PartnerSerializer
    class Meta:
        model = Job
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }
