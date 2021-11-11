from bridger.frontend import FrontendView
from bridger.routers import BridgerRouter
from django.urls import include, path
from rest_framework import routers, views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .api import ReligionViewSet, StudentDetail

router = BridgerRouter()
router.register(r"student", StudentDetail)
router.register(r"religion", ReligionViewSet, basename="religion")


urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    FrontendView.bundled_view("frontend/"),
    path("bridger/", include(("bridger.urls", "bridger"), namespace="bridger")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
