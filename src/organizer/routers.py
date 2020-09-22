from rest_framework.routers import SimpleRouter

from .viewsets import (
    TagViewSet,
    CompanyViewSet,
    PartnerViewSet,
    JobViewSet,
)

api_router = SimpleRouter()
api_router.register("tag", TagViewSet, base_name="api-tag")
api_router.register("company", CompanyViewSet, base_name="api-company")
api_router.register("partner", PartnerViewSet, base_name="api-partner")
api_router.register("job", JobViewSet, base_name="api-job")
api_routes = api_router.urls

urlpatterns = api_routes

