from django.urls import path

from .views.skills import SkillApiDetail, SkillApiList
from .views.experiences import (
    ExperienceApiList,
    ExperienceApiDetail,
)
from .views.institutions import (
    InstitutionApiList,
    InstitutionApiDetail,
)
from .views.educations import (
    EducationApiList,
    EducationApiDetail,
)
from .views.contacts import ContactApiList, ContactApiDetail
from .views.links import LinkApiList, LinkApiDetail
from .views.resumes import ResumeApiList, ResumeApiDetail
from .views.submissions import (
    ApplicationSubmissionApiList,
    ApplicationSubmissionApiDetail,
)


urlpatterns = [
    path(
        "skill/",
        SkillApiList.as_view(),
        name="api-skill-list",
    ),
    path(
        "skill/<str:slug>/",
        SkillApiDetail.as_view(),
        name="api-skill-detail",
    ),
    path(
        "experience/",
        ExperienceApiList.as_view(),
        name="api-experience-list",
    ),
    path(
        "experience/<str:slug>/",
        ExperienceApiDetail.as_view(),
        name="api-experience-detail",
    ),
    path(
        "institution/",
        InstitutionApiList.as_view(),
        name="api-institution-list",
    ),
    path(
        "institution/<str:slug>/",
        InstitutionApiDetail.as_view(),
        name="api-institution-detail",
    ),
    path(
        "education/",
        EducationApiList.as_view(),
        name="api-education-list",
    ),
    path(
        "education/<str:slug>/",
        EducationApiDetail.as_view(),
        name="api-education-detail",
    ),
    path(
        "contact/",
        ContactApiList.as_view(),
        name="api-contact-list",
    ),
    path(
        "contact/<str:slug>/",
        ContactApiDetail.as_view(),
        name="api-contact-detail",
    ),
    path(
        "link/", LinkApiList.as_view(), name="api-link-list"
    ),
    path(
        "link/<str:slug>/",
        LinkApiDetail.as_view(),
        name="api-link-detail",
    ),
    path(
        "resume/",
        ResumeApiList.as_view(),
        name="api-resume-list",
    ),
    path(
        "resume/<str:slug>/",
        ResumeApiDetail.as_view(),
        name="api-resume-detail",
    ),
    path(
        "submission/",
        ApplicationSubmissionApiList.as_view(),
        name="api-submission-list",
    ),
    path(
        "submission/<str:job_slug>/<str:resume_slug>/",
        ApplicationSubmissionApiDetail.as_view(),
        name="api-submission-detail",
    ),
]
