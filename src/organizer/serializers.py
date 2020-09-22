from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)
from .models import Tag, Company, Partner, Job


class TagSerializer(HyperlinkedModelSerializer):
    """Serializer for Tag data"""
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
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        exclude = ("id",)


class PartnerSerializer(CompanySerializer):
    """Serializer for Partner data"""
    class Meta:
        model = Partner
        exclude = ("id",)


class JobSerializer(ModelSerializer):
    """Serializer for Job data"""
    partner = HyperlinkedRelatedField(
        queryset=Partner.objects.all(),
        lookup_field="slug",
        view_name="api-partner-detail",
    )
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        exclude = ("id",)
