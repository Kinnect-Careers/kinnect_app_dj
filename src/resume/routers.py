from rest_framework.routers import SimpleRouter

from .viewsets import (
    SkillViewSet,
    ExperienceViewSet,
    TaskViewSet,
    InstitutionViewSet,
    EducationViewSet,
    ContactViewSet,
    LinkViewSet,
    ResumeViewSet,
    SubmissionViewSet,
)

api_router = SimpleRouter()
api_router.register("skill", SkillViewSet, base_name="api-skill")
api_router.register("experience", ExperienceViewSet, base_name="api-experience")
api_router.register("task", TaskViewSet, base_name="api-task")
api_router.register("contact", ContactViewSet, base_name="api-contact")
api_router.register("link", LinkViewSet, base_name="api-link")
api_router.register(
    "institution",
    InstitutionViewSet,
    base_name="api-institution")
api_router.register("education", EducationViewSet, base_name="api-education")
api_router.register("resume", ResumeViewSet, base_name="api-resume")
api_router.register("submission", SubmissionViewSet, base_name="api-submission")

api_routes = api_router.urls
