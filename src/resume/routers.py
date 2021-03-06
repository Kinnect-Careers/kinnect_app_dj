from rest_framework.routers import DefaultRouter

from .viewsets import (
    UserViewSet,
    GroupViewSet,
    SkillViewSet,
    ExperienceViewSet,
    InstitutionViewSet,
    EducationViewSet,
    PersonalViewSet,
    OtherViewSet,
    ResumeViewSet,
    SubmissionViewSet,
)

api_router = DefaultRouter()
api_router.register("user", UserViewSet, base_name="api-user")
api_router.register("group", GroupViewSet, base_name="api-group")
api_router.register("skill", SkillViewSet, base_name="api-skill")
api_router.register("experience", ExperienceViewSet, base_name="api-experience")
api_router.register("personal", PersonalViewSet, base_name="api-personal")
api_router.register("other", OtherViewSet, base_name="api-other")
api_router.register(
    "institution",
    InstitutionViewSet,
    base_name="api-institution")
api_router.register("education", EducationViewSet, base_name="api-education")
api_router.register("resume", ResumeViewSet, base_name="api-resume")
api_router.register("submission", SubmissionViewSet, base_name="api-submission")

urlpatterns = api_router.urls


