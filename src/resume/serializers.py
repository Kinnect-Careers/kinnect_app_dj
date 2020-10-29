from django.contrib.auth.models import User, Group
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    SlugRelatedField,
    ModelSerializer,
    ListSerializer,
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
        fields = '__all__'


class ComponentListSerializer(ListSerializer):
    def update(self, instance, validated_data):
        component_mapping = {component.id: component for component in instance}
        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for comp_id, data in data_mapping.items():
            component = component_mapping.get(comp_id, None)
            if component is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(componnt, data))

        for comp_id, component in component_mapping.items():
            if comp_id not in data_mapping:
                component.delete()
        return ret


class ContactSerializer(ModelSerializer):
    """Serializer for Contacts data"""

    def create(self, validated_data):
        contacts = self.Meta.model.objects.filter(contact=validated_data['contact'])
        if len(contacts) > 0:
            return contacts[0]
        else:
            return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.update(instance, **validated_data)
        return instance

    class Meta:
        model = Contact
        list_serializer_class = ComponentListSerializer
        fields = "__all__"


class LinkSerializer(ModelSerializer):
    """Serializer for Links data"""
    def create(self, validated_data):
        links = self.Meta.model.objects.filter(link=validated_data['link'])
        if len(links) > 0:
            return links[0]
        else:
            return self.Meta.model.objects.create(**validated_data)

    class Meta:
        model = Link
        list_serializer_class = ComponentListSerializer
        fields = "__all__"


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

    def create(self, data, *args, **kwargs):
        ModelClass = self.Meta.model
        new_instance = ModelClass.objects.create(title=data['title'])
        self.update(instance=new_instance, validated_data=data)
        return new_instance

    def update(self, instance, validated_data):
        # Adding contacts to resume instance
        contacts_data = validated_data.pop('contacts')
        contacts = instance.contacts
        contacts.clear()
        for contact in contacts_data:
            obj = Contact.objects.filter(contact=contact['contact'])[0]
            contacts.add(obj)

        # Adding links to resume instance
        links_data = validated_data.pop('links')
        links = instance.links
        links.clear()
        for link in links_data:
            obj = Link.objects.filter(link=link['link'])[0]
            links.add(obj)

        # Adding educational experiences to resume instance
        educations_data = validated_data.pop('educations')
        educations = instance.educations
        educations.clear()
        for ed in educations_data:
            obj = Education.objects.filter(
                degree=ed['degree'],
                institution=ed['institution'],
                started_at=ed['started_at']
            )[0]
            educations.add(obj)

        # Adding professional experiences to resume instance
        experiences_data = validated_data.pop('experiences')
        experiences = instance.experiences
        experiences.clear()
        for exp in experiences_data:
            obj = Experience.objects.filter(
                job_title=exp['job_title'],
                company=exp['company'],
                started_at=exp['started_at'],
                ended_at=exp['ended_at']
            )[0]
            experiences.add(obj)

        # Adding skills to resume instance
        skills_data = validated_data.pop('skills')
        skills = instance.skills
        skills.clear()
        for skill in skills_data:
            obj = Skill.objects.filter(name=skill['name'])[0]
            skills.add(obj)

        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class ApplicationSubmissionSerializer(ModelSerializer):
    """Serializer for Application Submission data"""
    resume = ResumeSerializer
    job = JobSerializer
    class Meta:
        model = ApplicationSubmission
        fields = "__all__"

