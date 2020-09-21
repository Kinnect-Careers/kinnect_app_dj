from django.urls import path

from .views.tags import TagApiDetail, TagApiList
from .views.companies import (
    CompanyApiList,
    CompanyApiDetail,
)
from .views.partners import (
    PartnerApiList,
    PartnerApiDetail
)
from .views.jobs import (
    JobApiList,
    JobApiDetail,
)

urlpatterns = [
    path(
        "company/",
        CompanyApiList.as_view(),
        name="api-company-list",
    ),
    path(
        "company/<str:slug>/",
        CompanyApiDetail.as_view(),
        name="api-company-detail",
    ),
    path(
        "partner/",
        PartnerApiList.as_view(),
        name="api-partner-list",
    ),
    path(
        "partner/<str:slug>/",
        PartnerApiDetail.as_view(),
        name="api-partner-detail",
    ),
    path("tag/", TagApiList.as_view(), name="api-tag-list"),
    path("tag/<str:slug>/", TagApiDetail.as_view(), name="api-tag-detail"),
    path("job/", JobApiList.as_view(), name="api-job-list"),
    path(
        "job/<str:partner_slug>/<str:job_slug>/",
        JobApiDetail.as_view(),
        name="api-job-detail",
    ),

]
