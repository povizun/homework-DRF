from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentListAPIView, UserCreateAPIView,
                         UserDestroyAPIView, UserListAPIView,
                         UserOtherRetrieveAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="user_list"),
    path("profile/", UserRetrieveAPIView.as_view(), name="profile"),
    path("update/", UserUpdateAPIView.as_view(), name="register"),
    path("delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("<int:pk>/", UserOtherRetrieveAPIView.as_view(), name="user_retrieve"),
]
