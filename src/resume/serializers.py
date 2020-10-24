from django.contrib.auth.models import User, Group
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    SlugRelatedField,
    ModelSerializer,
)
from .models import (
    Skill,
    Experience,
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


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


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


class ExperienceSerializer(ModelSerializer):
    """Serializer for Experience data"""
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
    #institution = SlugRelatedField(
    #    read_only=True,
    #    slug_field='name'
    #)
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
    contacts = ContactSerializer(many=True)
    links = LinkSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    educations = EducationSerializer(many=True)
    skills = SkillSerializer(many=True)

    def create(self, data, *args, **kwargs):
        ModelClass = self.Meta.model
        new_instance = ModelClass.objects.create(title=data['title'])
        self.update(instance=new_instance, validated_data=data)
        return new_instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        contacts = validated_data.get('contacts', None)
        if contacts:
            instance.contacts.clear()
            for contact in contacts:
                to_resume = Contact.objects.filter(contact=contact.get('contact'))
                if len(to_resume):
                    instance.contacts.add(to_resume[0])
            instance.save()
        links = validated_data.get('links', None)
        if links:
            instance.links.clear()
            for link in links:
                to_resume = Link.objects.filter(link=link.get('link'))
                if len(to_resume):
                    instance.links.add(to_resume[0])
            instance.save()
        experiences = validated_data.get('experiences', None)
        if experiences:
            instance.experiences.clear()
            for experience in experiences:
                to_resume = Experience.objects.filter(
                    company=experience.get('company'),
                    job_title=experience.get('job_title')
                )
                if len(to_resume):
                     instance.experiences.add(to_resume[0])
            instance.save()
        educations = validated_data.get('educations', None)
        if educations:
            instance.educations.clear()
            for ed in educations:
                to_resume = Education.objects.filter(
                    degree_type=ed.get('degree_type'),
                    degree=ed.get('degree'),
                    institution=ed.get('institution'),
                    started_at=ed.get('started_at'),
                    ended_at=ed.get('ended_at')
                )
                if len(to_resume):
                    instance.educations.add(to_resume[0])
            instance.save()
        skills = validated_data.get('skills', None)
        if skills:
            for skill in skills:
                to_resume = Skill.objects.filter(name=skill.get('name'))
                if len(to_resume):
                    instance.skills.add(to_resume[0])
            instance.save()
        return instance

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

