from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Skill
from ..serializers import SkillSerializer


class SkillApiDetail(APIView):
    def get(self, request, slug):
        skill = get_object_or_404(Skill, slug=slug)
        s_skill = SkillSerializer(
            skill,
            context={"request": request}
        )
        return Response(s_skill.data)


class SkillApiList(APIView):
    def get(self, request):
        skill_list = get_list_or_404(Skill)
        s_skill = SkillSerializer(
            skill_list,
            many=True,
            context={"request": request}
        )
        return Response(s_skill.data)
