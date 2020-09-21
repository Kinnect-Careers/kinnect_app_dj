from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
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


class CompanySerializer(ModelSerializer):
    """Serializer for Company data"""
    tags = TagSerializer(many=True)
    class Meta:
        model = Company
        fields = "__all__"


class PartnerSerializer(CompanySerializer):
    """Serializer for Partner data"""
    class Meta:
        model = Partner
        fields = "__all__"


class JobSerializer(ModelSerializer):
    """Serializer for Job data"""
    partner = PartnerSerializer
    tags = TagSerializer(many=True)
    class Meta:
        model = Job
        fields = "__all__"
