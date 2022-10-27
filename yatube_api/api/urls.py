from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register("posts", PostViewSet, basename="post")
router_v1.register("groups", GroupViewSet, basename="group")
router_v1.register("follow", FollowViewSet, basename="follow")
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path(
        "jwt/create/", TokenObtainPairView.as_view(), name="token_create"
    ),
    path(
        "jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path(
        "jwt/verify/", TokenVerifyView.as_view(), name="token_verify"
    ),
    path("", include(router_v1.urls)),
]
